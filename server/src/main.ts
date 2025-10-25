import { MikroORM } from "@mikro-orm/core";
import config from "../mikro-orm.config.js";
import { ClienteService, CriarClienteDTO } from "./modules/clientes/cliente.service.js";

const orm = await MikroORM.init(config);

const clienteService = new ClienteService(orm.em);

const user: CriarClienteDTO = {
    nomeCompleto: "Lucas Rech",
    documento: "12453345",
    senha: "1easdq313",
    numeroTelefone: "1123asqw",
};

console.log(await clienteService.criar(user));
