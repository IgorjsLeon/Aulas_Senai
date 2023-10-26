
class Filme:
    def __init__(self, titulo, genero, duracao, disponivel=True):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.disponivel = disponivel

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"Filme: {self.titulo}\nGênero: {self.genero}\nDuração: {self.duracao} minutos\nStatus: {status}"

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            return "Filme alugado com sucesso."
        else:
            return "Este filme não está disponível para locação."

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return "Filme devolvido com sucesso."
        else:
            return "Este filme já está disponível."

class Locadora:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []

    def adicionar_filme(self, *filmes):
        self.catalogo.extend(filmes)

    def listar_catalogo(self):
        print(f"Catálogo da Locadora {self.nome}:")
        for filme in self.catalogo:
            print(filme)

# Função principal para interagir com a locadora
def main():
    minha_locadora = Locadora("Minha Locadora")

    filme1 = Filme("Matrix", "Ação", 136)
    filme2 = Filme("O Poderoso Chefão", "Drama", 175)
    filme3 = Filme("Titanic", "Romance", 195)

    minha_locadora.adicionar_filme(filme1, filme2, filme3)

    while True:
        print("\nOpções:")
        print("1 - Listar Catálogo")
        print("2 - Alugar Filme")
        print("3 - Devolver Filme")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            minha_locadora.listar_catalogo()

        elif opcao == '2':
            titulo = input("Digite o título do filme que deseja alugar: ")
            for filme in minha_locadora.catalogo:
                if filme.titulo == titulo:
                    resultado = filme.alugar()
                    print(resultado)
                    break
                else:
                    print(f"Filme '{titulo}' não encontrado na locadora.")

        elif opcao == '3':
            titulo = input("Digite o título do filme que deseja devolver: ")
            for filme in minha_locadora.catalogo:
                if filme.titulo == titulo:
                    resultado = filme.devolver()
                    print(resultado)
                    break
                else:
                    print(f"Filme '{titulo}' não encontrado na locadora.")

        elif opcao == '4':
            print("Encerrando a aplicação.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

