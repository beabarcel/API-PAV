from src.model.Base import db
from src.model.MatrizQuantica import MatrizQuantica

def add_matriz_quantica(matriz: MatrizQuantica) -> MatrizQuantica:
    db.session.add(matriz)
    db.session.commit()
    return matriz

def get_matriz_quantica(id: int) -> MatrizQuantica:
    return MatrizQuantica.query.get(id)

def get_matrizes_quanticas() -> list[MatrizQuantica]:
    return MatrizQuantica.query.all()
