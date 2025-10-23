import { Collection, OneToMany, OneToOne, Property } from "@mikro-orm/core";
import { BaseEntity } from "../common/base.entity.js";
import { FormaPagamento } from "../common/enums.js";
import { Produto } from "../produtos/produto.entity.js";
import { Cliente } from "../clientes/cliente.entity.js";

export class Venda extends BaseEntity {

    @Property({nullable: false})
    formaPagamento!: FormaPagamento;

    @OneToMany({ mappedBy: "venda" })
    produtos = new Collection<Produto>(this);

    @OneToOne()
    cliente = Cliente;
}