import re
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.UsuarioService import add_usuario, get_usuario, get_usuarios

class UsuarioResponseSchema(Schema):
    id = fields.Int()
    nome_usuario = fields.Str()
    senha = fields.Str()
    data_cadastro = fields.DateTime()

class UsuarioRequestSchema(Schema):
    nome_usuario = fields.Str(required=True)
    senha = fields.Str(required=True)
    data_cadastro = fields.DateTime(required=True)

class UsuarioItem(MethodResource, Resource):
    @marshal_with(UsuarioResponseSchema)
    def get(self, usuario_id):
        try:
            usuario = get_usuario(usuario_id)
            if not usuario:
                abort(404, message="Resource not found")
            return usuario, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

class UsuarioList(MethodResource, Resource):
    @marshal_with(UsuarioResponseSchema(many=True))
    def get(self):
        try:
            return get_usuarios(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(UsuarioRequestSchema, location=("form"))
    @marshal_with(UsuarioResponseSchema)
    def post(self, **kwargs):
        try:
            usuario = add_usuario(**kwargs)
            return usuario, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
