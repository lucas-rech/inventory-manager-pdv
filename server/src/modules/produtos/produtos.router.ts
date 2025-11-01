import { MikroORM } from "@mikro-orm/mysql";
import { Router, type Request, type Response } from "express";
import config from "../../../mikro-orm.config.js";
import { CriarProdutoDTO, ProdutosService } from "./produtos.service.js";

const orm = await MikroORM.init(config);
const productService = new ProdutosService(orm.em);
const router = Router();

router.get("/buscar-todos", async (_req: Request, res: Response) => {
    const todosProdutos = await productService.buscarTodos();
    res.send(todosProdutos);
})

router.get("/buscar", async (req: Request, res: Response) => {
    const itemId = req.query.id;
    const produto = await productService.buscarporId(Number(itemId));

    res.send(produto);
})

router.post("/", async (req: Request<unknown, unknown, CriarProdutoDTO>, res: Response) => {
    console.log(req.body)
    const {nome, descricao, gtin, precoVenda, precoCusto } = req.body;

    res.send(await productService.criar({nome, descricao, gtin, precoVenda, precoCusto}));

});

export default router;
