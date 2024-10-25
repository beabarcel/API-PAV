from flask_restful import Resource

from src.controller.MatrizQuanticaController import MatrizQuanticaItem, MatrizQuanticaList
from src.controller.MedicaoController import MedicaoItem, MedicaoList
from src.controller.OperacaoController import OperacaoItem, OperacaoList
from src.controller.PortaQuanticaController import PortaQuanticaItem, PortaQuanticaList
from src.controller.UsuarioController import UsuarioItem, UsuarioList


def initialize_endpoints(api):

    api.add_resource(MatrizQuanticaItem, "/matriz-quantica/<int:porta_id>")
    api.add_resource(MatrizQuanticaList, "/matrizes-quanticas")

    api.add_resource(MedicaoItem, "/medicao/<int:medicao_id>")
    api.add_resource(MedicaoList, "/medicoes")

    api.add_resource(OperacaoItem, "/operacao/<int:operacao_id>")
    api.add_resource(OperacaoList, "/operacoes")

    api.add_resource(PortaQuanticaItem, "/porta-quantica/<int:porta_id>")
    api.add_resource(PortaQuanticaList, "/portas-quanticas")

    api.add_resource(UsuarioItem, "/usuario/<int:usuario_id>")
    api.add_resource(UsuarioList, "/usuarios")
