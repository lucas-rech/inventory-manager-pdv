import { Entity, PrimaryKey, Property } from "@mikro-orm/core";
import { ClienteRepository } from "./cliente.repository.js";

@Entity({ tableName: "clientes", repository: () => ClienteRepository })
export class Cliente {
    @PrimaryKey()
    id!: number;

    @Property({ length: 200, nullable: false })
    nomeCompleto!: string;

    @Property({ nullable: false })
    documento!: string;

    @Property({ nullable: false })
    senha!: string;
}
