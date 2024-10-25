import re
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.MedicaoService import add_medicao, get_medicao, get_medicoes

class MedicaoResponseSchema(Schema):
    id = fields.Int()
    id_matriz = fields.Int()
    data_medicao = fields.DateTime()

class MedicaoRequestSchema(Schema):
    id_matriz = fields.Int(required=True)
    data_medicao = fields.DateTime(required=True)

class MedicaoItem(MethodResource, Resource):
    @marshal_with(MedicaoResponseSchema)
    def get(self, medicao_id):
        try:
            medicao = get_medicao(medicao_id)
            if not medicao:
                abort(404, message="Resource not found")
            return medicao, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

class MedicaoList(MethodResource, Resource):
    @marshal_with(MedicaoResponseSchema(many=True))
    def get(self):
        try:
            return get_medicoes(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(MedicaoRequestSchema, location=("form"))
    @marshal_with(MedicaoResponseSchema)
    def post(self, **kwargs):
        try:
            medicao = add_medicao(**kwargs)
            return medicao, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
