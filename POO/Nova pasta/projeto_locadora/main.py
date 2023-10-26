from locadora import Locadora
from filme import Filme

def main():
    
    minha_locadora = Locadora("Minha Locadora")
    
    
    filme1 = Filme("Matrix", "Ação",225)
    filme2 = Filme("Curtindo a Vida","Comédia",90)
    filme3 = Filme("Tomates Verdes Fritos","Drama",120)

    minha_locadora.adicionar_filme(filme1)
    minha_locadora.adicionar_filme(filme2)
    minha_locadora.adicionar_filme(filme3)
    
    while True:
        print("\nOpções: ")
        print("Opção 1 - Listar Catálogo")
        print("Opção 2 - Alugar Filme")
        print("Opção 3 - Devolver Filme")
        print("Opção 4 - Sair")

        opcao = input("Escolha uma opção")

        if opcao == '1':
            minha_locadora.listar_catalogo()

        elif opcao == '2':
        
            titulo = input("Digite o título do filme ")
           
            for filme in minha_locadora.catalogo:
                if filme.titulo == titulo:
                    resultado = filme.alugar()
                    print(resultado)
                    break
            else:
                print(f"Fime '{titulo}'não encontrado na locadora.")

        elif opcao == "3":
            titulo = input("Digite o título do filme que deseja devolver ")
            for filme in minha_locadora.catalogo:
                resultado = filme.devolver()
                print(resultado)
                break
            else:
                print(f"Filme '{titulo}' não encontrado na locadora")
        
        elif opcao == '4':
            print("Encerrando aplicação")
            break

        else:
            print("Opção invalida!")

if __name__ == "__main__":
    main()



        
                




