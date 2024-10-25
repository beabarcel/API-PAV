from sqlalchemy import DateTime
from src.model.Usuario import Usuario
from src.repositories.UsuarioRepository import add_usuario, get_usuario, get_usuarios

def add_usuario_service(nome_usuario: str, senha: str, data_cadastro: DateTime) -> Usuario:
    novo_usuario = Usuario(
        nome_usuario=nome_usuario,
        senha=senha,
        data_cadastro=data_cadastro
    )
    return add_usuario(novo_usuario)

def get_usuario(id: int) -> Usuario:
    return get_usuario(id)

def get_usuarios() -> list[Usuario]:
    return get_usuarios()