#----------Importando as funções no arquivo funcoes.py--------------
from funcoes import menu_Estoque
from funcoes import inserir_Estoque
from funcoes import ver_Estoque
from funcoes import att_Estoque
from funcoes import exc_Estoque

#----------Criando o programa Estoque com as funções importadas---------

while True:
    menu_Estoque()
    opcao_Menu = int(input("Digite a opção desejada: "))

    if opcao_Menu == 1:
        codigo = float(input("Digite o código do produto: "))
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        inserir_Estoque(codigo, produto, quantidade)

    elif opcao_Menu == 2:
        ver_Estoque()

    elif opcao_Menu == 3:
        codigo = int(input("Digite o código do item que deseja atualizar: "))
        att_Estoque(codigo)

    elif opcao_Menu == 4:
        codigo = int(input("Digite o código do item a ser excluído: "))
        exc_Estoque(codigo)