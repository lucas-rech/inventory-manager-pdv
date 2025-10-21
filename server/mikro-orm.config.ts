import { MySqlDriver, Options } from "@mikro-orm/mysql";
import { TsMorphMetadataProvider } from "@mikro-orm/reflection";

const config: Options = {
    dbName: "nome-banco",
    user: "USUARIO",
    password: "SENHA",

    debug: true,
    driver: MySqlDriver,
    entities: ["dist/**/*.entity.js"],
    entitiesTs: ["src/**/*.entity.ts"],

    // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment
    metadataProvider: TsMorphMetadataProvider,
    allowGlobalContext: true,
};

export default config;
