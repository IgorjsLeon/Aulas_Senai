from cliente import Cliente

class Cadastro(Cliente):
    def __init__(self, nome, endereco, email, senha):
        self.senha = senha
        super().__init__(nome, endereco, email)

    def efetuar_cadastro(self):
        nome = input("Digite seu nome: ")
        endereco = input("Digite seu endereõ: ")
        email = input("Digite seu email: ")
        senha = int(input("Digite a sua senha: "))
        print(f"Bem-vindo(a) {nome}.")
        print(f"Seu endereço {endereco} e e-mail {email} foram cadastrados com sucesso.")
        print(f"Sua senha {senha} foi cadastrada com sucesso.")