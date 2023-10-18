#Crie um módulo em python, chamado clientes, onde você inseri, atualiza, le, delete clientes e incluir veiculo.

lista_Cliente = []

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

#-----------Criar função Ver Clientes-----------

def ver_Cliente():
    for cliente in lista_Cliente:
        print(f"Número do Cliente: {cliente['Numero Cliente']}, Cliente: {cliente['Nome']}, Telefone: {cliente['Telefone']}, E-mail: {cliente['E-mail']}, Marca: {cliente['Marca']}, Cor: {cliente['Cor']}, Placa: {cliente['Placa']}")
    
#------------------Menu Atualização------------------------

def menu_Att():
    print("----------------------------")
    print("-                           -")
    print("-   1 - Nome                -")
    print("-   2 - Telefone            -")
    print("-   3 - E-mail              -")
    print("-   4 - Marca do Veiculo    -")
    print("-   5 - Cor do Veiculo      -")
    print("-   6 - Placa do Veiculo    -")
    print("-                           -")
    print("-----------------------------")

#-----------Criar função Atualizar Clientes-----------

def att_Cliente_Nome(cliente):
    novo_Nome = input("Digite o novo nome: ")
    cliente['Nome'] = novo_Nome

def att_Cliente_Telefone(cliente):
    novo_Telefone = int(input("Digite o novo telefone: "))
    cliente['Telefone'] = novo_Telefone

def att_Cliente_Email(cliente):
    novo_Email = input("Digite o novo E-mail: ")
    cliente['E-mail'] = novo_Email

def att_Cliente_Marca(cliente):
    nova_Marca = input("Digite a nova marca do veiculo: ")
    cliente['Marca'] = nova_Marca

def att_Cliente_Cor(cliente):
    nova_Cor = input("Digite a nova cor do veiculo: ")
    cliente['Cor'] = nova_Cor

def att_Cliente_Placa(cliente):
    nova_Placa = input("Digite a nova placa do veiculo: ")
    cliente['Placa'] = nova_Placa

#-----------Criar função Excluír Cliente-----------

#----------Criar função Inserir Cliente + Veiculo ------------

def inserir_Clienteveiculo(num_Cliente, nome, telefone, email, marca, cor, placa):
    if not any(cliente['Numero Cliente'] == num_Cliente for cliente in lista_Cliente):
        lista_Cliente.append ({"Numero Cliente": num_Cliente, "Nome": nome, "Telefone": telefone, "E-mail": email, "Marca": marca, "Cor": cor, "Placa": placa})
        print("Cliente incluido com sucesso")
