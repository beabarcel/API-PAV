from src.model.Medicao import Medicao
from src.repositories.MedicaoRepository import add_medicao, get_medicao, get_medicoes
from datetime import datetime

def add_medicao_service(id_matriz: int, data_medicao: datetime) -> Medicao:
    nova_medicao = Medicao(
        id_matriz=id_matriz,
        data_medicao=data_medicao
    )
    return add_medicao(nova_medicao)

def get_medicao(id:int) -> Medicao:
    return get_medicao(id)

def get_medicoes() -> list[Medicao]:
    return get_medicoes()