import { Request } from "express";

export interface CriarProdutoDTO {
    nome: string;
    descricao?: string;
    gtin: string;
    precoVenda: number;
    precoCusto: number;
}

export interface ProdutoDTO {
    id: number;
    nome: string;
    descricao?: string;
    gtin: string;
    precoVenda: number;
    precoCusto: number;
    quantidadeEstoque: number;
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
    idProduto: number;
    custo: number;
    quantidadeLote: number;
    dataEntrada: Date;
    dataValidade: Date;
}

/// Interfaces de rotas
export interface CriarLoteRequestBody extends Request {
    body: CriarLoteDTO;
}
