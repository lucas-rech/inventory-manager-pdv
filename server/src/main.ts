import express from "express";
import { variables } from "./config/index.js";
import produtosRouter from "./modules/produtos/produtos.router.js";
import clientesRouter from "./modules/clientes/cliente.router.js";
import usuarioRouter from "./modules/admin/user.router.js";

const app = express();
app.use(express.json());
app.use("/produtos", produtosRouter);
app.use("/cliente", clientesRouter);
app.use("/usuario", usuarioRouter);

app.listen(variables.port, () => {
    console.log(`Web server rodando na porta ${variables.port.toString()}`);
});

/* 
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
}; */
