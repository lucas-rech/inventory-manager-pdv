import random

'''
!!!
Este arquivo é para apenas mostrar os clientes na tela do PDV,
após a integração com o banco de dados, pode retirar ele do projeto!!!
'''

# lista de nomes para sortear (40 nomes exemplo)
nomes = [
    "Ana", "Beatriz", "Carla", "Daniel", "Eduardo", "Fernanda", "Gustavo", "Helena",
    "Igor", "Juliana", "Karina", "Lucas", "Mariana", "Nicolas", "Olivia", "Paulo",
    "Renata", "Samuel", "Tatiana", "Vitor", "Amanda", "Bruno", "Cristina", "Diego",
    "Elisa", "Fabio", "Gabriela", "Henrique", "Isabela", "João", "Kátia", "Leandro",
    "Marcos", "Nicole", "Otávio", "Priscila", "Rafael", "Sofia", "Thiago", "Vanessa"
]

def gerar_cpf_raw():
    """Gera uma lista de 11 dígitos com dígitos verificadores corretos."""
    numeros = [random.randint(0, 9) for _ in range(9)]
    soma = sum([(10 - i) * numeros[i] for i in range(9)])
    resto = soma % 11
    d1 = 0 if resto < 2 else 11 - resto
    numeros.append(d1)

    soma = sum([(11 - i) * numeros[i] for i in range(10)])
    resto = soma % 11
    d2 = 0 if resto < 2 else 11 - resto
    numeros.append(d2)
    return numeros

def format_cpf(numeros):
    s = ''.join(map(str, numeros))
    return f"{s[:3]}.{s[3:6]}.{s[6:9]}-{s[9:]}"

def gerar_cpfs_unicos(qtd=20):
    seen = set()
    cpfs = []
    while len(cpfs) < qtd:
        nums = gerar_cpf_raw()
        cpf = format_cpf(nums)
        if cpf not in seen:
            seen.add(cpf)
            cpfs.append(cpf)
    return cpfs

# gera 20 CPFs únicos
cpfs = gerar_cpfs_unicos(20)

# escolhe 20 nomes aleatórios sem repetição (se tiver lista >= 20)
nomes_escolhidos = random.sample(nomes, len(cpfs))

# monta dicionário cpf -> nome
dicionario = {cpf: nome for cpf, nome in zip(cpfs, nomes_escolhidos)}

dicionario["33.240.005/0001-87"] = "Eu"
