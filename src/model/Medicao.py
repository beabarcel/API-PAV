from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .Base import Base, db

class Medicao(Base):
    __tablename__ = "medicao"

    id = Column(
        Integer, 
        primary_key=True
        )

    id_matriz = Column(
        Integer, 
        ForeignKey('matriz_quantica.id'), 
        nullable=False
        )

    data_medicao = Column(
        DateTime, 
        nullable=False
        )

    matriz = relationship(
        "MatrizQuantica", 
        back_populates="medicoes"
        )
