from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base, db

class Operacao(Base):
    __tablename__ = "operacao"

    id = Column(
        Integer, 
        primary_key=True
        )

    tipo_operacao = Column(
        String(150), 
        nullable=False
        )

    id_matriz_entrada = Column(
        Integer, 
        ForeignKey('matriz_quantica.id'), 
        nullable=False
        )
    id_matriz_resultado = Column(
        Integer, 
        ForeignKey('matriz_quantica.id'), 
        nullable=False
        )

    # Relacionamentos com a tabela MatrizQuantica
    matriz_entrada = relationship(
        "MatrizQuantica", 
        foreign_keys=[id_matriz_entrada], 
        back_populates="operacoes_entrada"
        )

    matriz_resultado = relationship(
        "MatrizQuantica", 
        foreign_keys=[id_matriz_resultado], 
        back_populates="operacoes_resultado"
        )
