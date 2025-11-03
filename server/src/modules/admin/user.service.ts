import { EntityManager, EntityRepository } from "@mikro-orm/mysql";
import { Usuario } from "./user.entity.js";
import { CriarUsuarioDTO } from "./user.interface.js";
import hash from "../../utils/hash-password.js";

export class UserService {
    private readonly em: EntityManager;
    private readonly usuarioRepo: EntityRepository<Usuario>;

    constructor(em: EntityManager) {
        this.em = em;
        this.usuarioRepo = this.em.getRepository(Usuario);
    }

    async criar(dto: CriarUsuarioDTO): Promise<Usuario> {
        if (await this.usuarioRepo.findOne({nickname: dto.nickname})) {
            throw new Error(`Já existe um usuário com o nickname ${dto.nickname}`)
        }

        const usuario = this.usuarioRepo.create(new Usuario(
            dto.nickname,
            dto.nomeCompleto,
            hash(dto.senha),
            dto.role,
            dto.numeroTelefone
        ));

        await this.em.persistAndFlush(usuario);
        return usuario;
    }

    async buscarPorNickname(nickname: string): Promise<Usuario> {
        const usuario = await this.usuarioRepo.findOne({nickname: nickname});

        if(!usuario) {
            throw new Error(`Não foi possível localizar um usuário com nickname ${nickname}`)
        };

        return usuario;
    }

}