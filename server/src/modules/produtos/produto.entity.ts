import { Collection, Entity, ManyToMany, OneToMany, Property } from "@mikro-orm/core";
import { BaseEntity } from "../common/base.entity.js";
import { Lote } from "./lotes/lote.entity.js";
import { Venda } from "../vendas/venda.entity.js";

@Entity({ tableName: "produtos" })
export class Produto extends BaseEntity {
    @Property({ length: 150, nullable: true })
    nome!: string;

    @Property({ length: 500, nullable: true })
    descricao?: string;

    @Property({ length: 14, nullable: false })
    gtin!: string;

    @OneToMany({ mappedBy: "produto" })
    lotes = new Collection<Lote>(this);

    @Property({ nullable: false })
    precoVenda!: number;

    @Property({ nullable: false })
    precoCusto!: number;

    @ManyToMany(() => Venda, (venda) => venda.produtos)
    vendas = new Collection<Venda>(this);
}
