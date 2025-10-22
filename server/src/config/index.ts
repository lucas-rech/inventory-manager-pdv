import dotenv from "dotenv";

dotenv.config();
export const variables = {
  port: process.env.PORT ?? 3000,
  db: {
    name: process.env.DB_NAME ?? "inventory_db",
    user: process.env.DB_USERNAME ?? "root",
    password: process.env.DB_PASSWORD ?? "password",
  }
};