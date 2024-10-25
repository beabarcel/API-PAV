from flask import Flask, app
from flask_restful import Api
from src.routes.endpoints import initialize_endpoints
from src.model.Base import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:232501@localhost:5432/pav'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return 'Aqui você gerencia suas matrizes quânticas! :)'

    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app