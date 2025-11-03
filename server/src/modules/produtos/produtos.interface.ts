import { Produto } from "./produto.entity.js";
import { Request } from "express";

export interface CriarProdutoDTO {
    nome: string;
    descricao?: string;
    gtin: string;
    precoVenda: number;
    precoCusto: number;
}

export interface AtualizarProdutoDTO {
    nome?: string;
    descricao?: string;
    gtin?: string;
    precoVenda?: number;
    precoCusto?: number;
}

export interface CriarLoteDTO {
    identificador: string;
    produto: Produto;
    custo: number;
    quantidadeLote: number;
    dataEntrada: Date;
    dataValidade: Date;
}

/// Interfaces de rotas
export interface CriarLoteRequestBody extends Request {
    body: CriarLoteDTO;
}
