import re
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.MatrizQuanticaService import add_matriz_quantica_service, get_matrizes_quanticas, get_matriz_quantica

class MatrizQuanticaResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    descricao = fields.Str()
    dimensao = fields.Int()
    eh_unitaria = fields.Bool()
    eh_hermitiana = fields.Bool()

class MatrizQuanticaRequestSchema(Schema):
    nome = fields.Str(required=True)
    descricao = fields.Str(required=True)
    dimensao = fields.Int(required=True)
    eh_unitaria = fields.Bool(required=True)
    eh_hermitiana = fields.Bool()

    @validates("nome")
    def validate_name(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_\s]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )

class MatrizQuanticaItem(MethodResource, Resource):
    @marshal_with(MatrizQuanticaResponseSchema)
    def get(self, matriz_id):
        try:
            matriz = get_matriz_quantica(matriz_id)
            if not matriz:
                abort(404, message="Resource not found")
            return matriz, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

class MatrizQuanticaList(MethodResource, Resource):
    @marshal_with(MatrizQuanticaResponseSchema(many=True))
    def get(self):
        try:
            return get_matrizes_quanticas(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(MatrizQuanticaRequestSchema, location=("form"))
    @marshal_with(MatrizQuanticaResponseSchema)
    def post(self, **kwargs):
        try:
            matriz = add_matriz_quantica_service(**kwargs)
            return matriz, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
