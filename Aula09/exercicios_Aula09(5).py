#Crie uma classe Tarefa que represente uma tarefa a ser realizada. A classe deve ter atributos como nome da tarefa, data de vencimento e status(pendente, em andamento, concluída). 
#Implemente métodos para marcar a tarefa como concluída.

class Tarefa:
    def __init__ (self, nome, data_vencimento):
        self.nome = nome
        self.data_vencimento = data_vencimento
        self.status = "Pendente"

    def marcar_tarefa_concluida(self):
        self.status = "Concluido"

    def veriricar_vencimento(self):
        data_tarefa = input("Digite a data da tarefa: ")
        if self.status == 'Pendente' and self.data_vencimento >= data_tarefa:
            return f"A tarefa {self.nome} está dentro do prazo"
        else:
            return f"A tarefa {self.nome} está atrasada..."
    
tarefa1 = Tarefa("Tirar o lixo", "2023-10-19")
print(tarefa1.veriricar_vencimento())
print(tarefa1.status)  

