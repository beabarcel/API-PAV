from src.model.Base import db
from src.model.Operacao import Operacao

def add_operacao(operacao: Operacao) -> Operacao:
    db.session.add(operacao)
    db.session.commit()
    return operacao

def get_operacao(id: int) -> Operacao:
    return Operacao.query.get(id)

def get_operacoes() -> list[Operacao]:
    return Operacao.query.all()
