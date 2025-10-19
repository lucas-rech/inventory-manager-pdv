from datetime import date
from sqlalchemy import (
    Column, Integer, String, Date, Float, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from core.database import engine  # seu engine já existente

Base = declarative_base() #Cria a base que as classes-modelo herdam para virar tabelas do banco.

Session = sessionmaker(bind=engine) #Fabrica sessões

#Classe Produto

class Produto(Base):
    __tablename__ = "produto" #define o nome da tabela no bd

    # colunas principais
    id = Column(Integer, primary_key=True, autoincrement=True)
    gtin = Column(String(50), unique=True, nullable=False)     # código de barras ou GTIN
    nome = Column(String(255), unique=True, nullable=False)
    descricao = Column(String(500), nullable=True)

    # relacionamento com Lote (um produto -> vários lotes)
    # back_populates cria ligação bidirecional com Lote.produto
    lotes = relationship(
        "Lote",
        back_populates="produto",
        cascade="all, delete-orphan",  # ao remover produto, remove seus lotes
        lazy="select"
    )

    def __repr__(self):
        return f"<Produto(id={self.id}, nome='{self.nome}', gtin='{self.gtin}')>"

    # === métodos de conveniência que interagem com o DB ===
    def adicionar_lote(self, session, lote):
        """
        Adiciona um lote associado a este produto.
        Parâmetros:
          - session: sessão SQLAlchemy ativa.
          - lote: instância de Lote (pode ter produto_id=None; será associada aqui).
        """
        lote.produto = self
        session.add(lote)
        session.commit()
        session.refresh(lote)  # atualiza atributos (id, por exemplo)
        return lote

    def remover_lote(self, session, lote_id):
        """
        Remove um lote deste produto pelo id.
        Retorna True se removeu, False se não encontrou.
        """
        lote = session.query(Lote).filter_by(id=lote_id, produto_id=self.id).first()
        if not lote:
            return False
        session.delete(lote)
        session.commit()
        return True

    def listar_lotes(self, session):
        """
        Retorna a lista de lotes associados a este produto.
        Pode retornar lista vazia.
        """
        # usando relacionamento já carregado / lazy load
        return session.query(Lote).filter_by(produto_id=self.id).all()

    def listar_lotes_vencidos(self, session, referencia: date):
        """
        Retorna lotes com data_validade < referencia (ou <= se preferir).
        'referencia' é um objeto datetime.date.
        """
        return session.query(Lote).filter(
            Lote.produto_id == self.id,
            Lote.data_validade < referencia
        ).all()


#Classe Lote 

class Lote(Base):
    __tablename__ = "lote"

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)
    codigo_lote = Column(String(100), nullable=True, unique=False)  # código do lote (opcional)
    quantidade = Column(Integer, nullable=False, default=0)
    data_entrada = Column(Date, nullable=True)
    data_validade = Column(Date, nullable=True)
    custo_unitario = Column(Float, nullable=True)

    # relação de volta pro produto
    produto = relationship("Produto", back_populates="lotes")

    def __repr__(self):
        return (f"<Lote(id={self.id}, produto_id={self.produto_id}, "
                f"codigo_lote='{self.codigo_lote}', quantidade={self.quantidade})>")


# cria tabelas (se já existem, ignora)
Base.metadata.create_all(engine)
