from src.model.MatrizQuantica import MatrizQuantica
from src.repositories.MatrizQuanticaRepository import (add_matriz_quantica, get_matriz_quantica, get_matrizes_quanticas  
)

def add_matriz_quantica_service(nome: str, descricao: str, dimensao: int, eh_unitaria: bool, eh_hermitiana: bool) -> MatrizQuantica:
    nova_matriz = MatrizQuantica(
        nome=nome,
        descricao=descricao,
        dimensao=dimensao,
        eh_unitaria=eh_unitaria,
        eh_hermitiana=eh_hermitiana
    )
    return add_matriz_quantica(nova_matriz)

def get_matriz_quantica_service(id: int) -> MatrizQuantica:
    return get_matriz_quantica(id)

def get_matrizes_quanticas() -> list[MatrizQuantica]:
    return get_matrizes_quanticas()  
