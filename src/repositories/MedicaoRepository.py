from src.model.Base import db
from src.model.Medicao import Medicao

def add_medicao(medicao: Medicao) -> Medicao:
    db.session.add(medicao)
    db.session.commit()
    return medicao

def get_medicao(id: int) -> Medicao:
    return Medicao.query.get(id)

def get_medicoes() -> list[Medicao]:
    return Medicao.query.all()
