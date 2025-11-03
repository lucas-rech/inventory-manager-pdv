import { EntityManager, EntityRepository, QueryOrder } from "@mikro-orm/mysql";
import { Produto } from "./produto.entity.js";
import { Lote } from "./lotes/lote.entity.js";
import { LoteRepository } from "./lotes/lote.repository.js";
import { AtualizarProdutoDTO, CriarLoteDTO, CriarProdutoDTO, ProdutoDTO } from "./produtos.interface.js";

export class ProdutosService {
    private readonly em: EntityManager;
    private readonly produtoRepo: EntityRepository<Produto>;
    private readonly loteRepo: LoteRepository;

    constructor(em: EntityManager) {
        this.em = em;
        this.produtoRepo = this.em.getRepository(Produto);
        this.loteRepo = this.em.getRepository(Lote);
    }

    async criar(dto: CriarProdutoDTO): Promise<Produto> {
        if (await this.produtoRepo.findOne({ gtin: dto.gtin })) {
            throw new Error(`Um produto com o GTIN ${dto.gtin} já existe`);
        }

        const produto = this.produtoRepo.create(new Produto(dto.nome, dto.gtin, dto.precoVenda, dto.precoCusto, dto.descricao));

        await this.em.persistAndFlush(produto);
        return produto;
    }

    async inserirNovoLote(dto: CriarLoteDTO): Promise<Lote> {
        const produto = await this.produtoRepo.findOne(dto.idProduto);
        if (!produto) {
            throw new Error(`Produto não existe`);
        }
        if (await this.loteRepo.findOne({ identificador: dto.identificador })) {
            throw new Error(`Já existe um lote com o identificador ${dto.identificador}`);
        }

        const lote = this.loteRepo.create(new Lote(dto.identificador, produto, dto.custo, dto.quantidadeLote, dto.dataEntrada, dto.dataValidade));
        await this.em.persistAndFlush(lote);

        return lote;
    }

    async buscarLotesDoProduto(productId: number): Promise<Lote[]> {
        const produto = await this.produtoRepo.findOne(productId);
        if (!produto) {
            throw new Error(`Produto com ID ${productId.toString()} não encontrado`);
        }

        const lotes = await this.loteRepo.findByProduct(productId);

        return lotes ?? [];
    }

    //Pode receber parâmetro de range, ordem etc.
    async buscarTodos(): Promise<Produto[]> {
        return await this.produtoRepo.findAll();
    }

    async buscarporId(id: number): Promise<ProdutoDTO> {
        const produto = await this.produtoRepo.findOne(id);

        if (!produto) {
            throw new Error(`Produto com ID ${id.toString()} não encontrado`);
        }

        const quantidadeEstoque = await this.calcularEstoqueTotal(id);

        const produtoDTO: ProdutoDTO = {
            id: produto.id,
            nome: produto.nome,
            descricao: produto.descricao,
            gtin: produto.gtin,
            precoVenda: produto.precoVenda,
            precoCusto: produto.precoCusto,
            quantidadeEstoque: quantidadeEstoque,
        };

        return produtoDTO;
    }

    async atualizar(id: number, dto: AtualizarProdutoDTO): Promise<Produto> {
        const produto = await this.produtoRepo.findOne(id);

        if (!produto) {
            throw new Error(`Produto com ID ${id.toString()} não encontrado`);
        }

        this.produtoRepo.assign(produto, dto);
        await this.em.flush();

        return produto;
    }

    async calcularEstoqueTotal(productId: number): Promise<number> {
        const lotes = (await this.loteRepo.findByProduct(productId)) ?? [];
        if (lotes.length === 0) {
            return 0;
        }

        let quantidadeTotal = 0;
        lotes.forEach((lote) => {
            quantidadeTotal += lote.quantidade;
        });
        return quantidadeTotal;
    }

    async remover(productId: number): Promise<Produto> {
        const produto = await this.produtoRepo.findOne(productId);

        if (!produto) {
            throw new Error("Produto não encontrado");
        }
        void this.em.removeAndFlush(produto);
        return produto;
    }

    //Consome do lote com data de validade mais próxima de vencer
    async consumirEstoque(productId: number, quantidade: number): Promise<number> {
        if (quantidade <= 0) {
            throw new Error("A quantidade a ser consumida deve ser maior que zero");
        }

        const produto = await this.produtoRepo.findOne(productId);
        if (!produto) {
            throw new Error(`Não foi possível encotnrar um produto com id ${productId.toString()}`);
        }

        const loteAntigo = await this.loteRepo.findOne({ produto: produto }, { orderBy: { dataValidade: QueryOrder.DESC } });

        if (!loteAntigo) {
            throw new Error(`Nenhum lote encontrado para o produto com id ${productId.toString()}`);
        }

        this.loteRepo.assign(loteAntigo, { quantidade: loteAntigo.quantidade - quantidade });
        await this.em.flush();

        return this.calcularEstoqueTotal(productId);
    }
}
