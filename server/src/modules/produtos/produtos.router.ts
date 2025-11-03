import { MikroORM } from "@mikro-orm/mysql";
import { Router, type Request, type Response } from "express";
import config from "../../../mikro-orm.config.js";
import { ProdutosService } from "./produtos.service.js";
import { AtualizarProdutoDTO, CriarLoteRequestBody, CriarProdutoDTO } from "./produtos.interface.js";

const orm = await MikroORM.init(config);
const productService = new ProdutosService(orm.em);
const router = Router();

router.get("/todos", async (_req: Request, res: Response) => {
    const todosProdutos = await productService.buscarTodos();
    try {
        res.send(todosProdutos);
    } catch (error) {
        res.status(500).send({ error: (error as Error).message });
    }
});

router.get("/buscar/:id", async (req: Request, res: Response) => {
    const itemId = req.params.id;
    try {
        const produto = await productService.buscarporId(Number(itemId));
        res.send(produto);
    } catch (error) {
        res.status(400).send({ error: (error as Error).message });
    }
});

router.post("/", async (req: Request<unknown, unknown, CriarProdutoDTO>, res: Response) => {
    console.log(req.body);
    const { nome, descricao, gtin, precoVenda, precoCusto } = req.body;

    try {
        res.send(await productService.criar({ nome, descricao, gtin, precoVenda, precoCusto }));
    } catch (error) {
        res.status(400).send({ error: (error as Error).message });
    }
});

router.put("/atualizar:id", async (req: Request<{ id: string }, unknown, AtualizarProdutoDTO>, res: Response) => {
    const itemId = req.params.id;
    if (!itemId) {
        res.status(400).send("ID do produto é obrigatório");
        return;
    }

    const dto = req.body;
    const produtoAtualizado = await productService.atualizar(Number(itemId), dto);
    try {
        res.send(produtoAtualizado);
    } catch (error) {
        res.status(400).send({ error: (error as Error).message });
    }
});

router.post("/consumir-estoque:id", async (req: Request<{ id: string }, unknown, { quantidade: number }>, res: Response) => {
    const itemId = req.params.id;
    const { quantidade } = req.body;

    if (!itemId) {
        res.status(400).send("ID do produto é obrigatório");
        return;
    }

    try {
        res.send(await productService.consumirEstoque(Number(itemId), quantidade));
    } catch (error) {
        res.status(400).send({ error: (error as Error).message });
    }
});

router.post("/consumir-estoque/:id", async (req: Request<{ id: string }>, res: Response) => {
    const id = req.params.id;
    const quantidade = Number(req.query.quantidade);

    if (!id) {
        res.status(400).send("ID do produto é obrigatório");
        return;
    } else if (isNaN(quantidade) || quantidade <= 0) {
        res.status(400).send("Quantidade inválida");
        return;
    }

    try {
        const quantidadeTotal = await productService.consumirEstoque(Number(id), quantidade);
        res.send({ mensagem: `Estoque consumido com sucesso. Nova quantidade em estoque: ${quantidadeTotal.toString()}` });
    } catch (error) {
        res.status(400).send({ error: (error as Error).message });
    }
});

router.post("/inserir-lote", async (req: CriarLoteRequestBody, res: Response) => {
    try {
        const { identificador, idProduto, custo, quantidadeLote, dataEntrada, dataValidade } = req.body;
        res.send(
            await productService.inserirNovoLote({
                identificador,
                idProduto,
                custo,
                quantidadeLote,
                dataEntrada: new Date(dataEntrada),
                dataValidade: new Date(dataValidade),
            }),
        );
    } catch (error) {
        res.status(400).send({ error: (error as Error).message });
    }
});

router.get("/lotes/:productId", async (req: Request, res: Response) => {
    try {
        const productId = Number(req.params.productId);
        const lotes = await productService.buscarLotesDoProduto(productId);
        res.send(lotes);
    } catch (error) {
        res.status(400).send({ error: (error as Error).message });
    }
});

export default router;
