import { EntityRepository } from "@mikro-orm/mysql";
import { Lote } from "./lote.entity.js";

export class LoteRepository extends EntityRepository<Lote> {
    async findByProduct(productId: number): Promise<Lote[] | null> {
        return this.find({ produto: productId });
    }
}
