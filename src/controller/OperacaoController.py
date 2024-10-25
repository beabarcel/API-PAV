import re
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.OperacaoService import add_operacao, get_operacao, get_operacoes

class OperacaoResponseSchema(Schema):
    id = fields.Int()
    tipo_operacao = fields.Str()
    id_matriz_entrada = fields.Int()
    id_matriz_resultado = fields.Int()

class OperacaoRequestSchema(Schema):
    tipo_operacao = fields.Str(required=True)
    id_matriz_entrada = fields.Int(required=True)
    id_matriz_resultado = fields.Int(required=True)

class OperacaoItem(MethodResource, Resource):
    @marshal_with(OperacaoResponseSchema)
    def get(self, operacao_id):
        try:
            operacao = get_operacao(operacao_id)
            if not operacao:
                abort(404, message="Resource not found")
            return operacao, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

class OperacaoList(MethodResource, Resource):
    @marshal_with(OperacaoResponseSchema(many=True))
    def get(self):
        try:
            return get_operacoes(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(OperacaoRequestSchema, location=("form"))
    @marshal_with(OperacaoResponseSchema)
    def post(self, **kwargs):
        try:
            operacao = add_operacao(**kwargs)
            return operacao, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
