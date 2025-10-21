import { Entity, PrimaryKey, Property } from "@mikro-orm/core";

@Entity({ tableName: "clientes" })
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
