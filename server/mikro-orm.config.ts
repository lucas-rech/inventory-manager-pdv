import { MySqlDriver, Options } from "@mikro-orm/mysql";
import { TsMorphMetadataProvider } from "@mikro-orm/reflection";
import { variables } from "./src/config/index.js";

const config: Options = {
    dbName: variables.db.name,
    user: variables.db.user,
    password: variables.db.password,

    debug: true,
    driver: MySqlDriver,
    entities: ["dist/**/*.entity.js"],
    entitiesTs: ["src/**/*.entity.ts"],

    // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment
    metadataProvider: TsMorphMetadataProvider,
    allowGlobalContext: true,
};

export default config;
