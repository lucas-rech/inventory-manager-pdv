import { type Request } from "express";

export interface CriarClienteDTO {
    nomeCompleto: string;
    documento: string;
    numeroTelefone?: string;
    senha: string;
}

export interface AtualizarClienteDTO {
    nomeCompleto?: string;
    documento?: string;
    numeroTelefone?: string;
    senha?: string;
}


export interface CriarClienteRequestBody extends Request {
    body: CriarClienteDTO;
}