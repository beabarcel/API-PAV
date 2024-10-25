import re

from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.FuncionarioService import updateFuncionario, getFuncionarios, deleteFuncionario, addFuncionario, getFuncionario


class FuncionarioResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    salario = fields.Float()

class FuncionarioRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    salario = fields.Float()
    
    @validates("nome")
    def validate_name(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_\s]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )
        
class FuncionarioItem(MethodResource, Resource):
    @marshal_with(FuncionarioResponseSchema)
    def get(self, funcionario_id):
        try:
            funcionario = getFuncionario(funcionario_id)
            if not funcionario:
                abort(404, message="Resource not found")
            return funcionario, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, funcionario_id):
        try:
            deleteFuncionario(funcionario_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(FuncionarioRequestSchema, location=("form"))
    @marshal_with(FuncionarioResponseSchema)
    def put(self, funcionario_id, **kwargs):
        try:
            funcionario = updateFuncionario(**kwargs, id=funcionario_id)
            return funcionario, 200
        except (OperationalError, IntegrityError):
           abort(500, message="Internal Server Error")


class FuncionarioList(MethodResource, Resource):
    @marshal_with(FuncionarioResponseSchema(many=True))
    def get(self):
        try:
            return getFuncionarios(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(FuncionarioRequestSchema, location=("form"))
    @marshal_with(FuncionarioResponseSchema)
    def post(self, **kwargs):
        try:
            funcionario = addFuncionario(**kwargs)
            return funcionario, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
