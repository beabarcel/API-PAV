from src.model.Base import db
from src.model.PortaQuantica import PortaQuantica

def add_porta_quantica(porta: PortaQuantica) -> PortaQuantica:
    db.session.add(porta)
    db.session.commit()
    return porta

def get_porta_quantica(id: int) -> PortaQuantica:
    return PortaQuantica.query.get(id)

def get_portas_quanticas() -> list[PortaQuantica]:
    return PortaQuantica.query.all()
