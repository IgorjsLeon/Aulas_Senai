class Filme:
    def __init__ (self, titulo, genero, duracao, disponivel = True):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.disponivel = disponivel
        
        
    def __str__(self):
        status = 'Disponivel' if self.disponivel else 'Indisponivel'
        return f'Filme: {self.titulo}.\n Gênero: {self.genero}.\n Duração: {self.duracao} minutos.\n Status: {status}.\n'
    
    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            return "Filme alugado com sucesso!"
        else:
            return f"{self.titulo}, não está disponivel para locação."
        
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print('Filme devolvido com sucesso!')
        else:
            return f'{self.titulo}, já está disponivel para alugar.'