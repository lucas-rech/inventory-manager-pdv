import { EntityManager, FindOptions } from "@mikro-orm/mysql";
import { ProdutoRepository } from "./produto.repository.js";
import { Produto } from "./produto.entity.js";

interface CriarProdutoDTO {
    nome: string;
    descricao?: string;
    gtin: string;
    precoVenda: number;
    precoCusto: number;
}

interface AtualizarProdutoDTO {
    nome?: string;
    descricao?: string;
    gtin?: string;
    precoVenda?: number;
    precoCusto?: number;
}

export class ProdutosService {
    private readonly em: EntityManager;
    private readonly produtoRepo: ProdutoRepository;

    constructor(em: EntityManager) {
        this.em = em;
        this.produtoRepo = this.em.getRepository(Produto);
    }

    async criar(dto: CriarProdutoDTO): Promise<Produto> {
        const produto = this.produtoRepo.create(new Produto(dto.nome, dto.gtin, dto.precoVenda, dto.precoCusto, dto.descricao));
        await this.em.persistAndFlush(produto);
        return produto;
    }

    //Pode receber parâmetro de range, ordem etc.
    async buscarTodos(options: FindOptions<Produto> = {}): Promise<Produto[]> {
        return this.produtoRepo.find({}, options);
    }

    async buscarporId(id: number): Promise<Produto> {
        const produto = await this.produtoRepo.findOne(id);

        if (!produto) {
            throw new Error(`Produto com ID ${id.toString()} não encontrado`);
        }

        return produto;
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
}
