import re
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.PortaQuanticaService import add_porta_quantica_service, get_porta_quantica, get_portas_quanticas

class PortaQuanticaResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    descricao = fields.Str()

class PortaQuanticaRequestSchema(Schema):
    nome = fields.Str(required=True)
    descricao = fields.Str()

class PortaQuanticaItem(MethodResource, Resource):
    @marshal_with(PortaQuanticaResponseSchema)
    def get(self, porta_id):
        try:
            porta = get_porta_quantica(porta_id)
            if not porta:
                abort(404, message="Resource not found")
            return porta, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

class PortaQuanticaList(MethodResource, Resource):
    @marshal_with(PortaQuanticaResponseSchema(many=True))
    def get(self):
        try:
            return get_portas_quanticas(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(PortaQuanticaRequestSchema, location=("form"))
    @marshal_with(PortaQuanticaResponseSchema)
    def post(self, **kwargs):
        try:
            porta = add_porta_quantica_service(**kwargs)
            return porta, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
