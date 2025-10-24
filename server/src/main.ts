import { MikroORM } from "@mikro-orm/core";
import { Cliente } from "./modules/clientes/cliente.entity.js";
import config from "../mikro-orm.config.js";

const orm = await MikroORM.init(config);

//Exemplo de criação de usuário
const user = new Cliente();
user.nomeCompleto = "lucas rech";
user.documento = "123455667";
user.senha = "asd2342edas";
await orm.em.persist(user).flush();
