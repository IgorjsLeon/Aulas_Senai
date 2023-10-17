#Crie um módulo em python, chamado clientes, onde você inseri, atualiza, le, delete clientes e incluir veiculo.

#------------------Menu------------------------

lista_Cliente = []

def menu_Cliente():
    print("\n----------------------------------")
    print("-   Lista de Clientes  em Python   -")
    print("-     by: Igor Leon                -")
    print("-                                  -")
    print("-   1 - Inserir Cliente            -")
    print("-   2 - Inserir Veiculo            -")
    print("-   3 - Ver Clientes               -")
    print("-   4 - Atualizar Cliente          -")
    print("-   5 - Excluír Cliente            -")
    print("-                                  -")
    print("------------------------------------")

#-----------Criar função Inserir Cliente-----------

def inserir_Cliente(cliente, nome, telefone, email):
    if cliente not in lista_Cliente:
        lista_Cliente.append ({"Nome": nome, "Telefone": telefone, "E-mail": email})
        print("Cliente incluido com sucesso")

#-----------Criar função Inserir Veiculo-----------

def inserir_Veiculo(veiculo, marca, cor, placa):
    if veiculo not in lista_Cliente:
        lista_Cliente.append ({"Marca": marca, "Cor": cor, "Placa": placa})
        print("Veiculo incluido com sucesso")

#-----------Criar função Ver Clientes-----------

def ver_Cliente():
    print(lista_Cliente)
    

#-----------Criar função Atualizar Clientes-----------
#-----------Criar função Excluír Cliente-----------

#----------Criar função Inserir Cliente + Veiculo ------------

def inserir_Clienteveiculo(cliente, nome, telefone, email, marca, cor, placa):
    if cliente not in lista_Cliente:
        lista_Cliente.append ({"Nome": nome, "Telefone": telefone, "E-mail": email, "Marca": marca, "Cor": cor, "Placa": placa})
        print("Cliente incluido com sucesso")

