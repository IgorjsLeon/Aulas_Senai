#----------Importando as funções no arquivo calculadora.py--------------
from funcoes_Calculadora import menu_Calculadora
from funcoes_Calculadora import soma
from funcoes_Calculadora import sub
from funcoes_Calculadora import mult
from funcoes_Calculadora import div

#----------Criando o Programa da Calculadora--------------

while True:
    menu_Calculadora()
    
    opcao_Menu = int(input("Digite a opção desejada: "))

    if opcao_Menu == 1:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        print(f"Resultado: {soma(num1, num2)}")
    elif opcao_Menu == 2:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        sub(num1, num2)
        print(f"Resultado: {sub(num1, num2)}")
    elif opcao_Menu == 3:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        mult(num1, num2)
        print(f"Resultado: {mult(num1, num2)}")
    elif opcao_Menu == 4:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        div(num1, num2)
        print(f"Resultado: {div(num1, num2)}")
