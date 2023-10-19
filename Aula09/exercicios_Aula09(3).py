#Crie uma classe Pessoa que possui um atributo de classe para manter o número de pessoas criadas. Cada vez que você instancia um objeto da classe Pessoa, o contador deve ser incrementado.

class Pessoa:
    total_pessoas = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

pressoa1 = Pessoa('Alisse', 15)
pessoa2 = Pessoa('Carlos', 25)
print(Pessoa.total_pessoas)