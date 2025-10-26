import { Entity, Property } from "@mikro-orm/core";
import { BaseEntity } from "../common/base.entity.js";

@Entity({ tableName: "produtos" })
export class Produto extends BaseEntity {
    @Property({ length: 150, nullable: true })
    nome!: string;

    @Property({ length: 500, nullable: true })
    descricao?: string;

    @Property({ length: 14, nullable: false })
    gtin!: string;

    @Property({ nullable: false, type: "double" })
    precoVenda!: number;

    @Property({ nullable: false, type: "double" })
    precoCusto!: number;

    constructor(nome: string, gtin: string, precoVenda: number, precoCusto: number, descricao?: string) {
        super();
        this.nome = nome;
        this.descricao = descricao ?? "null";
        this.gtin = gtin;
        this.precoVenda = precoVenda;
        this.precoCusto = precoCusto;
    }
}
