import { Entity, ManyToOne, Property } from "@mikro-orm/core";
import { BaseEntity } from "../../common/base.entity.js";
import { Produto } from "../produto.entity.js";
import { LoteRepository } from "./lote.repository.js";

@Entity({ tableName: "lotes", repository: () => LoteRepository })
export class Lote extends BaseEntity {
    @Property({ nullable: false })
    identificador!: string;

    @ManyToOne(() => Produto)
    produto!: Produto;

    @Property({ nullable: false })
    custo!: number;

    @Property({ nullable: false })
    quantidade!: number;

    @Property({ nullable: false, type: "date" })
    dataEntrada!: Date;

    @Property({ nullable: false, type: "date" })
    dataValidade!: Date;

    constructor(identificador: string, produto: Produto, custo: number, quantidade: number, dataEntrada: Date, dataValidade: Date) {
        super();
        this.identificador = identificador;
        this.produto = produto;
        this.custo = custo;
        this.quantidade = quantidade;
        this.dataEntrada = dataEntrada;
        this.dataValidade = new Date(dataValidade.getFullYear(), dataValidade.getMonth(), dataValidade.getDay());
    }
}
