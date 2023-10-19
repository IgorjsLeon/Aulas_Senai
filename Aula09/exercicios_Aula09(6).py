#Neste projeto, você deve criar uma calculadora interativa que utiliza a classe Calculadora para realizar operações.

#---------Criando a classe---------
class Calculadora:
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def somar(num1, num2):
        return num1 + num2
    
    def sub(num1, num2):
        return num1 - num2
    
    def mult(num1, num2):
        return num1 * num2
    
    def div(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Não é possivel dividir 0."

#----------importando funções---------

from funcoes_padroes import menu_calculadora

#---------Criando programa---------

while True:
    menu_calculadora()
    opcao_menu = input("Digite a opção desejada: ")

    if opcao_menu == "1":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print(Calculadora.somar(num1, num2))
    elif opcao_menu == "2":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print(Calculadora.sub(num1, num2))
    elif opcao_menu == "3":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print(Calculadora.mult(num1 , num2))
    elif opcao_menu == "4":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print(Calculadora.div(num1, num2))
    elif opcao_menu == "5":
        print("Obrigado por utilizar o meu programa ;-).\n")
        break
    else:
        print("Opção invalida!")