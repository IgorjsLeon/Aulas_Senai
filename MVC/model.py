class Tarefas:
    def __init__ (self, descricao, concluida = False):
        self.descricao = descricao
        self.concluida = concluida

class ListaTarefaModelo: #Possivel herança
    def __init__(self):
        self.tarefa = []
    
    def adicionar_tarefa(self, tarefa):
        self.tarefa.append(tarefa)

    def obter_tarefa (self):
        return self.tarefa