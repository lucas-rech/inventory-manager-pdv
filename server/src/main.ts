import { MikroORM } from "@mikro-orm/core";
import config from "../mikro-orm.config.js";
import { ClienteService, CriarClienteDTO } from "./modules/clientes/cliente.service.js";
import { CriarLoteDTO, CriarProdutoDTO, ProdutosService } from "./modules/produtos/produtos.service.js";

const orm = await MikroORM.init(config);

const clienteService = new ClienteService(orm.em);
const productService = new ProdutosService(orm.em);

const user: CriarClienteDTO = {
    nomeCompleto: "Lucas Rech",
    documento: "12453345",
    senha: "1easdq313",
    numeroTelefone: "1123asqw",
};

const product: CriarProdutoDTO = {
    nome: "Bombom",
    gtin: "12345678901234",
    descricao: "muuuuuuuuuuuuuuuuooooito bom",
    precoCusto: 1.5,
    precoVenda: 30.0,
};

console.log(await productService.criar(product));
console.log(await clienteService.criar(user));

const lote: CriarLoteDTO = {
    identificador: "1234534",
    produto: await productService.buscarporId(1),
    quantidadeLote: 50,
    custo: 200.0,
    dataEntrada: new Date(),
    dataValidade: new Date(2025, 10, 30),
};
console.log(await productService.inserirNovoLote(lote));

console.log(await productService.inserirNovoLote(lote));
console.log(await productService.calcularEstoqueTotal(1));

console.log(await productService.consumirEstoque(1, 20));
