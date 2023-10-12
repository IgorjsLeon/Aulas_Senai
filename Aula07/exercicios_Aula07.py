#Crie uma calculadora com todas as operações basicas usando as funções.
from calculadora import menu_Estoque
from calculadora import inserir_Estoque
from calculadora import ler_Estoque
while True:
    menu_Estoque()
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        codigo = int(input("Digite o código do produto: "))
        nome = input("Digite o produto: ")
        quantidade = int(input("Digite a quantidade: "))
        inserir_Estoque(codigo, nome, quantidade)
        
    elif opcao == 2:
        ler_Estoque()