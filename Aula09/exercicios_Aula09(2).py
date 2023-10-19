#Crie uma classe aluno que possui atributos como nome, idade e notas. Implemente métodos para calcular a média das notas e verificar se o aluno foi aprovado (média maior ou igual a 6).

#-------------------Criando a classe Aluno-------------------

class Aluno:
    def __init__ (self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

#-------------------Criando a função Calculo Média-------------------

    def calculo_Media(nota1, nota2, nota3):
        return nota1 + nota2 + nota3 / 3

#-------------------Criando a função Verificar Aprovação do aluno-------------------

    def verificar_Aprovacao(self, media):
        media = self.calculo_Media()
        if media < 6:
            print(f"Aluno reporvado com média: {media}.")
        else:
            print(f"Aluno aprovado com média: {media}.")



teste = Aluno('junhinho', 10, [4, 5, 10])