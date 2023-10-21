#-----------Classe Veiculo-----------

class Veiculo:
    def __init__ (self, nome, marca, modelo, potencia, combustivel, n_passageiros):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.combustivel = combustivel
        self.n_passagieros = n_passageiros

#-----------Herança-----------

class Automovel(Veiculo):
    def __init__(self, nome, marca, modelo, potencia, combustivel, n_passageiros, cor):
        self.cor = cor
        super().__init__(nome, marca, modelo, potencia, combustivel, n_passageiros) #Essa função vai fazer com que o programa inicie primeiro o metodo construtor da classe mãe (Veiculo) e depois a classe filha (Automovel).

#-----------Classe Aluno-----------

class Pessoa:
    def __init__(self, nome, sobrenome, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco

#-----------Herança-----------

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, endereco, matricula, curso):
        self.matricula = matricula
        self.curso = curso
        super().__init__(nome, sobrenome, endereco)

#-----------Herança multipla-----------

#class Moto(Veiculo, Pessoa): a classe Moto herda a classe Veiculo e Pessoa.



'''Uma plataforma de locação de filmes, series e documentarios, onde teremos o Banco(realizar pagamentos), Cartão de credito, Locação, Catalogo, Login.'''