import { Role } from "../common/enums.js";
import { type Request } from "express";

export interface CriarUsuarioDTO {
    nickname: string,
    nomeCompleto: string,
    role: Role,
    numeroTelefone: string,
    senha: string
}

export interface ResponseUsuarioDTO {
    id: number,
    nickname: string,
    nomeCompleto: string,
    role: Role,
    numeroTelefone: string,
    senha: string
}

export interface LoginRequestDTO {
    nickname: string,
    senha: string
}


export interface CriarUsuarioRequestBody extends Request {
    body: CriarUsuarioDTO;
}

export interface LoginRequestBody extends Request {
    body: LoginRequestDTO
}