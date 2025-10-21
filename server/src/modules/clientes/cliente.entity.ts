import { Entity, PrimaryKey, Property } from "@mikro-orm/core";
<<<<<<< HEAD

@Entity({ tableName: "clientes" })
=======
import { ClienteRepository } from "./cliente.repository.js";

@Entity({ tableName: "clientes", repository: () => ClienteRepository})
>>>>>>> 3a0133359c87bb345b81e433fd69f22b1831746d
export class Cliente {
    @PrimaryKey()
    id!: number;

    @Property({ length: 200, nullable: false })
    nomeCompleto!: string;

    @Property({ nullable: false })
    documento!: string;

    @Property({ nullable: false })
    senha!: string;
}
