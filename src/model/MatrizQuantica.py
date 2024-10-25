from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from .Base import Base, db

class MatrizQuantica(Base):
    __tablename__ = "matriz_quantica"

    id = Column(
        Integer, 
        primary_key=True
        )

    nome = Column(
        String(50), 
        nullable=False
        )

    descricao = Column(
        String(100), 
        nullable=False
        )

    dimensao = Column(
        Integer, 
        nullable=False
        )
        
    eh_unitaria = Column(
        Boolean, 
        nullable=False
        )

    eh_hermitiana = Column(
        Boolean, 
        nullable=True
        )

    data_criacao = Column(
        DateTime,
        nullable=False
        )

    # Relationship com outras tabelas
    medicoes = relationship(
        "Medicao", 
        back_populates="matriz"
        )

    operacoes_entrada = relationship(
        "Operacao", 
        foreign_keys="[Operacao.id_matriz_entrada]", 
        back_populates="matriz_entrada"
        )

    operacoes_resultado = relationship(
        "Operacao", 
        foreign_keys="[Operacao.id_matriz_resultado]", 
        back_populates="matriz_resultado"
        )
