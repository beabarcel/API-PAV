from src.model.PortaQuantica import PortaQuantica
from src.repositories.PortaQuanticaRepository import add_porta_quantica

def add_porta_quantica_service(nome: str, descricao: str = None) -> PortaQuantica:
    nova_porta = PortaQuantica(
        nome=nome,
        descricao=descricao
    )
    return add_porta_quantica(nova_porta)

def get_porta_quantica(id: int) -> PortaQuantica:
    return get_porta_quantica(id)

def get_portas_quanticas() -> list[PortaQuantica]:
    return get_portas_quanticas()
