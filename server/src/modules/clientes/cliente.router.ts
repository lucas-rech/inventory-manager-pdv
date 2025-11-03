import { MikroORM } from "@mikro-orm/core";
import config from "../../../mikro-orm.config.js";
import { Router, type Response } from "express";
import { CriarClienteRequestBody } from "./cliente.interface.js";
import { ClienteService } from "./cliente.service.js";

const orm = await MikroORM.init(config);
const clienteService = new ClienteService(orm.em);
const router = Router();

router.post("/", async (req: CriarClienteRequestBody, res: Response) => {
    try {
        const { nomeCompleto, documento, numeroTelefone, senha } = req.body;
        await clienteService.criar({
                nomeCompleto,
                documento,
                numeroTelefone,
                senha
            })
        
        res.status(200);
    } catch (error) {
        res.status(400).send({error: (error as Error).message})
    }
});


export default router;