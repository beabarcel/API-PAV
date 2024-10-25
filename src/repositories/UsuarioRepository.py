from src.model.Base import db
from src.model.Usuario import Usuario

def add_usuario(usuario: Usuario) -> Usuario:
    db.session.add(usuario)
    db.session.commit()
    return usuario

def get_usuario(id: int) -> Usuario:
    return Usuario.query.get(id)

def get_usuarios() -> list[Usuario]:
    return Usuario.query.all()
