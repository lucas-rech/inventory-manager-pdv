"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var mysql_1 = require("@mikro-orm/mysql");
var reflection_1 = require("@mikro-orm/reflection");
var index_js_1 = require("./src/config/index.js");
var cliente_entity_js_1 = require("./src/modules/clientes/cliente.entity.js");
var produto_entity_js_1 = require("./src/modules/produtos/produto.entity.js");
var lote_entity_js_1 = require("./src/modules/produtos/lotes/lote.entity.js");
var venda_entity_js_1 = require("./src/modules/vendas/venda.entity.js");
var produto_venda_entity_js_1 = require("./src/modules/vendas/produto-venda.entity.js");
var config = {
    dbName: index_js_1.variables.db.name,
    user: index_js_1.variables.db.user,
    password: index_js_1.variables.db.password,
    debug: true,
    driver: mysql_1.MySqlDriver,
    entities: ["dist/**/*.entity.js"],
    entitiesTs: [cliente_entity_js_1.Cliente, produto_entity_js_1.Produto, lote_entity_js_1.Lote, venda_entity_js_1.Venda, produto_venda_entity_js_1.ProdutoVenda],
    metadataProvider: reflection_1.TsMorphMetadataProvider,
    allowGlobalContext: true,
};
exports.default = config;
