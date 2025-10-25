import { Collection, Entity, ManyToMany, ManyToOne, Property } from "@mikro-orm/core";
import { BaseEntity } from "../common/base.entity.js";
import { FormaPagamento } from "../common/enums.js";
import { Produto } from "../produtos/produto.entity.js";
import { Cliente } from "../clientes/cliente.entity.js";

@Entity({ tableName: "vendas" })
export class Venda extends BaseEntity {
    @Property({ nullable: false, type: "string" })
    formaPagamento!: FormaPagamento;

    @ManyToMany(() => Produto)
    produtos = new Collection<Produto>(this);

    @ManyToOne(() => Cliente)
    cliente!: Cliente;

    @Property({nullable: false, type: "numeric"})
    totalVenda!: number;
}
