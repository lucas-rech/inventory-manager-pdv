import { EntityManager } from "@mikro-orm/mysql";
import { ClienteRepository } from "./cliente.repository.js";
import { Cliente } from "./cliente.entity.js";
import { AtualizarClienteDTO, CriarClienteDTO } from "./cliente.interface.js";
import hash from "../../utils/hash-password.js";


export class ClienteService {
    private readonly em: EntityManager;
    private readonly clienteRepo: ClienteRepository;

    constructor(em: EntityManager) {
        this.em = em;
        this.clienteRepo = this.em.getRepository(Cliente);
    }

    async criar(dto: CriarClienteDTO): Promise<Cliente> {
        if (await this.clienteRepo.findByDocumento(dto.documento)) {
            throw new Error(`Usuário com o documento ${dto.documento} já existe`);
        }

        const cliente = this.clienteRepo.create(new Cliente(dto.nomeCompleto, dto.documento, hash(dto.senha), dto.numeroTelefone));
        await this.em.persistAndFlush(cliente);

        return cliente;
    }

    async encontrarPorDucumento(doc: string): Promise<Cliente> {
        const cliente = await this.clienteRepo.findByDocumento(doc);

        if (!cliente) {
            throw new Error(`Nenhum cliente encontrado com o documento ${doc}`);
        }
        return cliente;
    }

    async encontrarPorId(id: number): Promise<Cliente> {
        const cliente = await this.clienteRepo.findOne(id);
        if (!cliente) {
            throw new Error(`Não existe um cliente com o id ${id.toString()}`);
        }
        return cliente;
    }

    async atualizarCliente(id: number, dto: AtualizarClienteDTO): Promise<Cliente> {
        const cliente = await this.clienteRepo.findOne(id);

        if (!cliente) {
            throw new Error(`Nenhum cliente encontrado com o id ${id.toString()}`);
        }
        this.clienteRepo.assign(cliente, dto);
        await this.em.flush();

        return cliente;
    }
}
