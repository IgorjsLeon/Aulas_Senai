#----------Criação da variavel estoque----------------

estoque = {}

#----------Criar menu por função-----------

def menu_Estoque():
    print("\n--------------------------")
    print("-   Estoque em Python    -")
    print("-     by: Igor Leon      -")
    print("-                        -")
    print("-   1 - Inserir Produto  -")
    print("-   2 - Ver Estoque      -")
    print("-   3 - Atualizar        -")
    print("-   4 - Excluír          -")
    print("-                        -")
    print("--------------------------")

#-----------Criar função Inserir Produto-----------

def inserir_Estoque(codigo, produto, quantidade):
    if codigo not in estoque:
        estoque[codigo] = {"produto": produto, "quantidade": quantidade}
    else:
        print("Produto ja existente em estoque, por gentileza utileze o a opção 3-Atualizar do menu.")

#-----------Criar função Ver Estoque-----------

def ver_Estoque():
    for produtos in estoque:
        print(estoque[produtos])

#-----------Criar função Atualizar-----------

def att_Estoque(codigo):
    if codigo in estoque:
        nova_Quantidade = int(input("Digite a nova quantidade: "))
        estoque[codigo]["quantidade"] = nova_Quantidade
    else:
        print("Produto não encontrado no estoque.")

#-----------Criar função Excluír-----------

def exc_Estoque(codigo):
    if codigo in estoque:
        del estoque[codigo]
    else:
        print("Produto não encontrado no estoque.")
