import { Collection, OneToMany, Property } from "@mikro-orm/core";
import { BaseEntity } from "../common/base.entity.js";
import { Lote } from "./lotes/lote.entity.js";

export class Produto extends BaseEntity {
  
  @Property({length: 150, nullable: true})
  nome!: string;

  @Property({ length: 500, nullable: true })
  descricao?: string;

  @Property({ length: 14, nullable: false })
  gtin!: string;

  @OneToMany({ mappedBy: "produto" })
  lotes = new Collection<Lote>(this);

  @Property({ nullable: false })
  precoVenda!: number;

}