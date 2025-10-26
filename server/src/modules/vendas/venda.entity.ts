import { Entity, ManyToOne, Property } from "@mikro-orm/core";
import { BaseEntity } from "../common/base.entity.js";
import { FormaPagamento } from "../common/enums.js";
import { Cliente } from "../clientes/cliente.entity.js";

@Entity({ tableName: "vendas" })
export class Venda extends BaseEntity {
    @Property({ nullable: false, type: "string" })
    formaPagamento!: FormaPagamento;

    @ManyToOne()
    cliente!: Cliente;

    @Property({ nullable: false, type: "numeric" })
    valorTotal!: number;
}
