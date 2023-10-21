from filme import Filme, Serie, Documentario
from cliente import Cliente
from login import Login


print("#############################")
print("# Bem-vindo(a) ao SenaiFlix #")
print("#        By: IgorLeon       #")
print("#############################")

login = Login(email = input("Digite o seu E-mail: "), senha = int(input("Digite a sua senha: ")))
login.efetua_login()

#----------------Inicia Programa----------------

while True:
    print("----------------------------------------")
    print("-       1 - Alugar Filmes              -")
    print("-       2 - Alugar Série               -")
    print("-       3 - Alugar Documentario        -")
    print("-       4 - Sair                       -")
    print("----------------------------------------")

    opcao = input("Digite a opção desejada: ")

    #----------------Inicia Alugar Filme----------------

    if opcao == '1':
        while True:
            break



    #----------------Fecha o Programa----------------
    elif opcao == '5':
        print("Obrigado por utilizar o meu serviço ;-).")
        break
    else:
        print("Opção invalida.")