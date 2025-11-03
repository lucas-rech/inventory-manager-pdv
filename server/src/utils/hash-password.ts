import bcrypt from "bcrypt";

export default function hashPassword(valor: string) {
    const saltRounds = 10;
    return bcrypt.hashSync(valor, saltRounds)
}