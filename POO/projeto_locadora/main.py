from locadora import Locadora
from filme import Filme

def main():

    minha_locadora = Locadora("Leon's Location")
    
    filme1 = Filme('Matrix', 'Ação', 225)
    filme2 = Filme('Barraca do Beijo', 'Romance', 140)
    filme3 = Filme('Curtindo a Vida', 'Comédia', 120)

    minha_locadora.adicionar_filme(filme1)
    minha_locadora.adicionar_filme(filme2)
    minha_locadora.adicionar_filme(filme3)
    

    while True:
        print("\n--------------------------")
        print("-   Locadora  em Python   -")
        print("-     by: Igor Leon       -")
        print("-                         -")
        print("-   1 - Listar Catálogo   -")
        print("-   2 - Alugar Filme      -")
        print("-   3 - Devolver Filme    -")
        print("-   4 - Sair              -")
        print("-                         -")
        print("---------------------------")

        opcao_menu = input("Digite a opção desejada: ")

        if opcao_menu == '1':
            minha_locadora.listar_catalogo()

        elif opcao_menu == '2':
            titulo = input("Digite o título do filme desejado: ")
            for filme in minha_locadora.catalogo:
                if filme.titulo == titulo:
                    resultado = filme.alugar()
                    print(resultado)
                    break
            else:
                print(f"{titulo}, não encontrado!")
                

        elif opcao_menu == '3':
            titulo = input("Digite o título do filme a ser devolvido: ")
            for filme in minha_locadora.catalogo:
                if filme == filme1:
                    resultado = filme1.devolver()
                    break
                elif filme == filme2:
                    resultado = filme2.devolver()
                    break
                elif filme == filme3:
                    resultado = filme3.devolver()
                    break
            else:
                print(f"{titulo}, não encontrado.")
                

        elif opcao_menu == '4':
            print("Obrigado por utilziar o meu serviço.\n")
            break

        else:
            print("Opção inválida.")

main()

#fazer um projeto agenda, vai ter a classe Contato(nome, telefone, e-mail) que são atributos obrigatorios e uma classe Agenda ela vai ter um metodo construtor que recebe uma lista de contatos vazia, vai ter metodo add contato,
#listar contato, buscar contatos e deletar contatos.