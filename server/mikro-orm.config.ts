import { MySqlDriver, Options } from "@mikro-orm/mysql";
import { TsMorphMetadataProvider } from "@mikro-orm/reflection";
import { variables } from "./src/config/index.js";
import { Cliente } from "./src/modules/clientes/cliente.entity.js";
import { Produto } from "./src/modules/produtos/produto.entity.js";
import { Lote } from "./src/modules/produtos/lotes/lote.entity.js";
import { Venda } from "./src/modules/vendas/venda.entity.js";

const config: Options = {
    dbName: variables.db.name,
    user: variables.db.user,
    password: variables.db.password,

    debug: true,
    driver: MySqlDriver,
    entities: ["dist/**/*.entity.js"],
    entitiesTs: [Cliente, Produto, Lote, Venda],

    metadataProvider: TsMorphMetadataProvider,
    allowGlobalContext: true,
};

export default config;
