import { Entity, Property } from "@mikro-orm/core";
import { BaseEntity } from "../common/base.entity.js";
import { Role } from "../common/enums.js";

@Entity({ tableName: "usuarios" })
export class Usuario extends BaseEntity {

    @Property({ length: 50, nullable: false })
    nickname!: string;

    @Property({ length: 200, nullable: false })
    nomeCompleto!: string;

    @Property({ nullable: false, type: "string" })
    role!: Role

    @Property({ length: 20, nullable: true })
    numeroTelefone?: string;

    @Property({ nullable: false })
    senha!: string;

    constructor(nickname: string, nomeCompleto: string, senha: string, role: Role, numeroTelefone?: string) {
        super();
        this.nickname = nickname;
        this.nomeCompleto = nomeCompleto;
        this.role = role;
        this.senha = senha;
        this.numeroTelefone = numeroTelefone;
    }
}
