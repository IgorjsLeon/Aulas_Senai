def menu_Calculadora():
    print("\n#####################################")
    print("#                                   #")
    print("# Bem-vindo à calculadora em Python #")
    print("#          by Igor Leon             #")
    print("#                                   #")
    print("#####################################")
    print("--------------------------------")
    print("-       1 - Adição             -")
    print("-       2 - Subtração          -")
    print("-       3 - Multiplicação      -")
    print("-       4 - Divisão            -")
    print("--------------------------------")
    

def soma(num1, num2):
    return (num1 + num2)

def sub(num1, num2):
   return (num1 - num2)

def mult(num1, num2):
    return (num1 * num2)

def div(num1, num2):
    return (num1 / num2)

"""menu_Calculadora()

opcao_Menu = int(input("Digite a opção desejada: "))
if opcao_Menu == 1:
    num1 = int(input("numero 1: "))
    num2 = int(input("numero 2: "))
    print(soma(num1,num2))
elif opcao_Menu == 2:
    num1 = int(input("numero 1: "))
    num2 = int(input("numero 2: "))
    print(sub(num1,num2))
elif opcao_Menu == 3:
    num1 = int(input("numero 1: "))
    num2 = int(input("numero 2: "))
    print(mult(num1,num2))
elif opcao_Menu == 4:
    num1 = int(input("numero 1: "))
    num2 = int(input("numero 2: "))
    print(div(num1,num2))
    """

#Inserir, ler, atualizar e excluir um item no estoque.
"""creat = inserir ou criar                                                         
read = ler
update = atualizar
delete = excluir
estoque ["chave"] = valor
"""
estoque = {}
def menu_Estoque():
        print("--------------------")
        print("-      Estoque     -")
        print("-                  -")
        print("-   1- Inserir     -")
        print("-   2- Ler         -")
        print("-   3- Atualizar   -")
        print("-   4- Excluir     -")
        print("-                  -")
        print("--------------------")
             
def inserir_Estoque(codigo, nome, quantidade):
    if codigo not in estoque:
        estoque[codigo] = {"nome": nome, "quantidade": quantidade}
    else:
        print("O item já existe no estoque.")

def ler_Estoque():
    for i in estoque:
        print(estoque[i])