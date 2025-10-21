import { EntityRepository } from "@mikro-orm/mysql";
import { Cliente } from "./cliente.entity.js";

export class ClienteRepository extends EntityRepository<Cliente> {
    
}