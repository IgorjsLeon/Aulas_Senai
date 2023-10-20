#Crie um módulo em python, chamado clientes, onde você inseri, atualiza, le, delete clientes e incluir veiculo.

lista_clientes = []

#------------------Menu Geral------------------------

def menu_Cliente():
    print("\n----------------------------------")
    print("-   Lista de Clientes  em Python   -")
    print("-     by: Igor Leon                -")
    print("-                                  -")
    print("-   1 - Inserir Cliente + Veiculo  -")
    print("-   2 - Ver Clientes               -")
    print("-   3 - Atualizar Cliente          -")
    print("-   4 - Excluír Cliente            -")
    print("-                                  -")
    print("------------------------------------")

#----------Criar função Inserir Cliente + Veiculo ------------

def inserir_cliente_veiculo(num_cliente, nome, telefone, email, marca, placa, cor):
    cliente = {'Número do cliente': num_cliente,
                        'Nome': nome,
                        'Telefone': telefone,
                        'E-mail': email,
                        'Marca': marca,
                        'Placa': placa,
                        'Cor': cor}
    lista_clientes.append(cliente)


#-----------Criar função Ver Clientes-----------

def ver_cliente():
    ordenar_clientes = sorted(lista_clientes, key=lambda x: x['Número do cliente'])
    for cliente in ordenar_clientes:
        print(cliente)
    
#------------------Menu Atualização------------------------

def menu_Att():
    print("----------------------------")
    print("-                           -")
    print("-   1 - Nome                -")
    print("-   2 - Telefone            -")
    print("-   3 - E-mail              -")
    print("-   4 - Marca do Veiculo    -")
    print("-   5 - Placa do Veiculo    -")
    print("-   6 - Cor do Veiculo      -")
    print("-                           -")
    print("-----------------------------")

#-----------Criar função Atualizar Clientes-----------

def att_Cliente_Nome(num_cliente, novo_Nome):
    for num_cliente in lista_clientes:
        if num_cliente['Número do cliente'] == num_cliente:
            num_cliente['Nome'] = novo_Nome
            break
    

def att_Cliente_Telefone():
    ordenar_clientes = sorted(lista_clientes, key=lambda x: x['Número do cliente'])
    for cliente in ordenar_clientes:
        novo_Telefone = int(input("Digite o novo telefone: "))
        cliente['Telefone'] = novo_Telefone

def att_Cliente_Email():
    ordenar_clientes = sorted(lista_clientes, key=lambda x: x['Número do cliente'])
    for cliente in ordenar_clientes:
        novo_Email = input("Digite o novo E-mail: ")
        cliente['E-mail'] = novo_Email

def att_Cliente_Marca():
    ordenar_clientes = sorted(lista_clientes, key=lambda x: x['Número do cliente'])
    for cliente in ordenar_clientes:
        nova_Marca = input("Digite a nova marca do veiculo: ")
        cliente['Marca'] = nova_Marca

def att_Cliente_Cor():
    ordenar_clientes = sorted(lista_clientes, key=lambda x: x['Número do cliente'])
    for cliente in ordenar_clientes:
        nova_Cor = input("Digite a nova cor do veiculo: ")
        cliente['Cor'] = nova_Cor

def att_Cliente_Placa():
    ordenar_clientes = sorted(lista_clientes, key=lambda x: x['Número do cliente'])
    for cliente in ordenar_clientes:
        nova_Placa = input("Digite a nova placa do veiculo: ")
        cliente['Placa'] = nova_Placa

#-----------Criar função Excluír Cliente-----------



