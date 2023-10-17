#Nome de classe sempre em letra maiuscula!
"""
class Automovel:
    def __init__(self, modelo, marca, cor):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor

automovel1 = Automovel("Mustang", "Ford", "Azul")

monolitico = um sistema feito em bloco unico (um depende do outro) [alto aclopamento e baixa coesão]
sistema de micro-serviços = um sistema feito em diversos blocos e caso um pare os outros continuam funcionando normal.
alta coesão = classes independentes
baixa coesão = classes dependentes de outras classes
aclopamento = classes interligadas"""


"""class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcula_area(self, base, altura):
        res = base * altura
        return res
    
retangulo_1 = Retangulo()
retangulo_1.calcula_area()
"""

#Crie uma classe chamada aluno (Nome, idade, e-mail), (o aluno pergunta)

class Aluno:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def perguntar(pergunta):
        pergunta = input("Digite sua pergunta: ")
        print(pergunta)

aluno = Aluno("Igor", "26", "igor@igor")
aluno.perguntar()