import { EntityRepository } from "@mikro-orm/mysql";
import { Produto } from "./produto.entity.js";

export class ProdutoRepository extends EntityRepository<Produto> {
    /* ... */
}
