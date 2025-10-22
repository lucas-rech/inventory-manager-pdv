import { Property } from "@mikro-orm/core";
import { BaseEntity } from "../common/base.entity.js";

export class Lote extends BaseEntity {

    @Property({nullable: false})
    identificador!: string;

    @Property({nullable: false})
    custo!: number;

    @Property({nullable: false})
    quantidade!: number;

    @Property({nullable: false})
    dataEntrada!: Date;

    @Property({nullable: false})
    dataValidade!: Date;
}