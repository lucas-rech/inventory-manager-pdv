import { MikroORM } from "@mikro-orm/mysql";
import { Router, type Request, type Response } from "express";
import config from "../../../mikro-orm.config.js";
import { ProdutosService } from "./produtos.service.js";
import { AtualizarProdutoDTO, CriarLoteRequestBody, CriarProdutoDTO } from "./produtos.interface.js";

const orm = await MikroORM.init(config);
const productService = new ProdutosService(orm.em);
const router = Router();

router.get("/buscar-todos", async (_req: Request, res: Response) => {
    const todosProdutos = await productService.buscarTodos();
    res.send(todosProdutos);
});

router.get("/buscar:id", async (req: Request, res: Response) => {
    const itemId = req.query.id;
    const produto = await productService.buscarporId(Number(itemId));

    res.send(produto);
});

router.post("/", async (req: Request<unknown, unknown, CriarProdutoDTO>, res: Response) => {
    console.log(req.body);
    const { nome, descricao, gtin, precoVenda, precoCusto } = req.body;

    res.send(await productService.criar({ nome, descricao, gtin, precoVenda, precoCusto }));
});

router.post("/inserir-lote", async (req: CriarLoteRequestBody, res: Response) => {
    const { identificador, produto, custo, quantidadeLote, dataEntrada, dataValidade } = req.body;
    res.send(await productService.inserirNovoLote({ identificador, produto, custo, quantidadeLote, dataEntrada, dataValidade }));
});

router.put("/atualizar:id", async (req: Request<{ id: string }, unknown, AtualizarProdutoDTO>, res: Response) => {
    const itemId = req.params.id;
    if (!itemId) {
        res.status(400).send("ID do produto é obrigatório");
        return;
    }

    const dto = req.body;
    const produtoAtualizado = await productService.atualizar(Number(itemId), dto);
    res.send(produtoAtualizado);
});

router.post("/consumir-estoque:id", async (req: Request<{ id: string }, unknown, { quantidade: number }>, res: Response) => {
    const itemId = req.params.id;
    const { quantidade } = req.body;

    if (!itemId) {
        res.status(400).send("ID do produto é obrigatório");
        return;
    }

    res.send(await productService.consumirEstoque(Number(itemId), quantidade));
});

export default router;
