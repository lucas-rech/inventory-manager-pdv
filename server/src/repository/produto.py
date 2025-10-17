from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from model import Produto
from sqlalchemy.orm import Session

from core.logger import LOGGER


def criar_produto(session: Session, produto: Produto) -> Produto:
    '''
    Cria um novo produto na tabela de produtos do banco de dados.
    
    :param Session session: Sessão do banco de dados no SQLAlchemy.
    :param Produto produto: Objeto(modelo) de um produto para ser criado na tabela de produtos do banco de dados.
    
    :return: Produto
    '''
    
    try:
        session.add(produto) #adiciona um produto
        session.commit() #commita na sessão atual a alteração
        LOGGER.success(f"Novo produto criado: {produto}")
        return produto
    except IntegrityError as e:
        LOGGER.error(f"IntegrityError ao criar produto: {e}")
    except SQLAlchemyError as e:
        LOGGER.error(f"SQLAlchemyError ao criar produto: {e}")
    except Exception as e:
        LOGGER.error(f"Erro inesperado ao criar produto: {e}")
        
        
        
        
        
    