import bcrypt from "bcrypt";

export default function hash(valor: string, saltRounds: number) {
    return bcrypt.hashSync(valor, saltRounds)
}