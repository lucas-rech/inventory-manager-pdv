import { Entity, ManyToOne, Property } from "@mikro-orm/core";
import { BaseEntity } from "../../common/base.entity.js";
import { Produto } from "../produto.entity.js";
import { LoteRepository } from "./lote.repository.js";

@Entity({ tableName: "lotes", repository: () => LoteRepository})
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
