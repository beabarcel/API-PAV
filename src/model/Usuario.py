from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .Base import Base, db

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(
        Integer, 
        primary_key=True
        )

    nome_usuario = Column(
        String(100), 
        nullable=False
        )

    senha = Column(
        String(150), 
        nullable=False
        )

    data_cadastro = Column(
        DateTime, 
        nullable=False
        )
