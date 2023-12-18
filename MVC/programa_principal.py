from model import ListaTarefaModelo
from view import ListaTarefasVisao
from controller import ListaTarefasController

def principal():
    model = ListaTarefaModelo()
    view = ListaTarefasVisao()
    controller = ListaTarefasController(model, view)
    controller.executar()

principal()