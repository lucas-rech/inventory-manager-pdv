import { Entity, ManyToOne, Property } from "@mikro-orm/core";
import { BaseEntity } from "../../common/base.entity.js";
import { Produto } from "../produto.entity.js";

@Entity({ tableName: "lotes" })
export class Lote extends BaseEntity {
    @Property({ nullable: false })
    identificador!: string;

    @ManyToOne(() => Produto)
    produto!: Produto;

    @Property({ nullable: false })
    custo!: number;

    @Property({ nullable: false })
    quantidade!: number;

    @Property({ nullable: false })
    dataEntrada!: Date;

    @Property({ nullable: false })
    dataValidade!: Date;

}
