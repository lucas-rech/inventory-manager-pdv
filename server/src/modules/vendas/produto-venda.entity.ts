import { Entity, ManyToOne, PrimaryKeyProp, Property } from "@mikro-orm/core";
import { Produto } from "../produtos/produto.entity.js";
import { Venda } from "./venda.entity.js";

@Entity()
export class ProdutoVenda {
    @ManyToOne({ primary: true })
    produto!: Produto;

    @ManyToOne({ primary: true })
    venda!: Venda;

    @Property()
    quantidade!: number;

    @Property({ type: "decimal", precision: 10, scale: 2 })
    precoUnitario!: number;

    [PrimaryKeyProp]?: ["venda", "produto"];

    constructor(produto: Produto, venda: Venda, quantidade: number, precoUnitario: number) {
        this.produto = produto;
        this.venda = venda;
        this.quantidade = quantidade;
        this.precoUnitario = precoUnitario;
    }
}
