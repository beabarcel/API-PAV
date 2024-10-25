from src.model.Operacao import Operacao
from src.repositories.OperacaoRepository import add_operacao

def add_operacao_service(tipo_operacao: str, id_matriz_entrada: int, id_matriz_resultado: int) -> Operacao:
    nova_operacao = Operacao(
        tipo_operacao=tipo_operacao,
        id_matriz_entrada=id_matriz_entrada,
        id_matriz_resultado=id_matriz_resultado
    )
    return add_operacao(nova_operacao)

def get_operacao (id: int) -> Operacao:
    return get_operacao(id)

def get_operacoes() -> list[Operacao]:
    return get_operacoes()