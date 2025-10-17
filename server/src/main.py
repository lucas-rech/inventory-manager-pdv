from core.database import get_session
from core.logger import LOGGER
from model import Produto
from repository.produto import criar_produto


def main():
    LOGGER.info("Iniciando aplicação...")

    session = get_session()

    #Exemplo de criação de produto
    novo_produto = Produto(
        gtin="1234567890123",
        nome="Produto Exemplo",
        descricao="Um produto de teste."
    )

    criar_produto(session, novo_produto)

    LOGGER.success("Execução finalizada com sucesso!")


if __name__ == "__main__":
    main()
