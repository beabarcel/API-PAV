from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base, db

class PortaQuantica(Base):
    __tablename__ = "porta_quantica"

    id = Column(
        Integer, 
        primary_key=True
        )

    nome = Column(
        String, 
        nullable=False
        )
        
    descricao = Column(
        String, 
        nullable=True
        )
