import { EntityRepository } from "@mikro-orm/mysql";
import { Cliente } from "./cliente.entity.js";

export class ClienteRepository extends EntityRepository<Cliente> {
    async findByDocumento(doc: string): Promise<Cliente | null> {
        return this.findOne({ documento: doc });
    }

    async findByNumeroTelefone(numero: string): Promise<Cliente | null> {
        return this.findOne({ numeroTelefone: numero });
    }
}
