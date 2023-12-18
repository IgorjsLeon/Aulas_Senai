class ListaTarefasVisao:
    def mostrar_tarefa(self, tarefa):
        print('Lista de tarefas: ')
        for i, tarefa in enumerate(tarefa, start=1):
            status = 'Concluida' if tarefa.concluida else 'Pendente'
            print(f'{i}.{tarefa.descricao} - {status}')

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def obter_entrada_usuario(self, prompt):
        return input(prompt)