import { Entity, Property } from "@mikro-orm/core";
import { ClienteRepository } from "./cliente.repository.js";
import { BaseEntity } from "../common/base.entity.js";

@Entity({ tableName: "clientes", repository: () => ClienteRepository })
export class Cliente extends BaseEntity {
    @Property({ length: 200, nullable: false })
    nomeCompleto!: string;

    @Property({ nullable: false })
    documento!: string;

    @Property({ length: 20, nullable: true })
    numeroTelefone?: string;

    @Property({ nullable: false })
    senha!: string;

    constructor(nomeCompleto: string, documento: string, senha: string, numeroTelefone?: string) {
        super();
        this.nomeCompleto = nomeCompleto;
        this.documento = documento;
        this.senha = senha;
        this.numeroTelefone = numeroTelefone;
    }
}
