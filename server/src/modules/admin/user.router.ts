import { MikroORM } from "@mikro-orm/core";
import config from "../../../mikro-orm.config.js";
import { UserService } from "./user.service.js";
import { Router, type Response } from "express";
import { CriarUsuarioRequestBody, LoginRequestBody } from "./user.interface.js";
import bcrypt from "bcrypt";

const orm = await MikroORM.init(config);
const userService = new UserService(orm.em);
const router = Router();

router.post("/registrar", async (req: CriarUsuarioRequestBody, res: Response) => {
    try {
        const {nickname, nomeCompleto, role, numeroTelefone, senha} = req.body;
        await userService.criar({
            nickname,
            nomeCompleto,
            senha,
            role,
            numeroTelefone
        })

        res.status(200).send();
        
    } catch (error) {
        res.status(400).send({error: (error as Error).message})
    }
})

router.post("/login", async (req: LoginRequestBody, res: Response) => {
    try {
        const {nickname, senha} = req.body;
        const usuario = await userService.buscarPorNickname(nickname);

        if(bcrypt.compareSync(senha, usuario.senha)) {
            res.status(201).send({token: "234h23i4u23i4asdffqr"});
        } else {
            res.status(401).send({error: "Senha inválida"});
        }
    } catch (error) {
        res.status(400).send({error: (error as Error).message})
    }
})

export default router;