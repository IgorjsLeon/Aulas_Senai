"""pilhas = voce retira os objetos 1 por 1 de cima
fila = primeiro que entra é o primeiro que sai.
def custo_Mercadoria_Vendida(estoque_Inicial, estoque_Final, compras):
    cmv = (estoque_Final + compras - estoque_Inicial)
    print("O estoque atual é de:", cmv)
def valor_Compras_Periodo(estoque_Inicial, estoque_Final):
    valor_Compras_Periodo = (estoque_Final - estoque_Inicial)
    print("O valor compras:", valor_Compras_Periodo)
    """


from funcoes_Clientes import menu_Cliente, inserir_cliente_veiculo, ver_cliente, menu_Att, att_Cliente_Nome, att_Cliente_Telefone, att_Cliente_Email, att_Cliente_Marca, att_Cliente_Cor, att_Cliente_Placa

lista_clientes = []
cliente_existente = []
while True:
    menu_Cliente()
    opcao_menu = input("Digite a opção desejada: ")
    if opcao_menu == '1':
        num_cliente = int(input("Digite o número do cliente: "))
        if num_cliente in cliente_existente:
            print("Cliente já existe, utilize a opção 3 para atualiza-lo.")
        else:
            nome = input("Digite o nome completo do cliente: ")
            telefone = int(input("Digite o telefone do cliente: "))
            email = input("Digite o e-mail do cliente: ")
            marca = input("Digite a marca do veículo do cliente: ")
            placa = input("Digite a marca do veículo do cliente: ")
            cor = input("Digite a cor do veículo do cliente: ")
            inserir_cliente_veiculo(num_cliente, nome, telefone, email, marca, placa, cor)
            cliente_existente.append(num_cliente)
            print("Cliente cadastrado com sucesso.")
        
    elif opcao_menu == '2':
        ver_cliente()

    elif opcao_menu == '3':
        menu_Att()
        opcao_menu = input("Digite a opção desejada: ")
        #------Nome------
        if opcao_menu == '1':
            num_cliente = int(input("Digite o número do cliente: "))
            if num_cliente in cliente_existente:
               novo_Nome = input("Digite o novo nome: ")
               att_Cliente_Nome(num_cliente,novo_Nome)
            else:
                print("Cliente não encontrado.")
        #------Telefone------
        elif opcao_menu == '2':
            num_cliente = int(input("Digite o número do cliente: "))
            if num_cliente in cliente_existente:
                att_Cliente_Telefone()
                print("Telefone alterado com sucesso.")
            else:
                print("Cliente não encontrado.")
        #------E-mail------
        elif opcao_menu == '3':
            num_cliente = int(input("Digite o número do cliente: "))
            if num_cliente in cliente_existente:
                att_Cliente_Email()
                print("E-mail alterado com sucesso.")
            else:
                print("Cliente não encontrado.")
        #------Marca------
        elif opcao_menu == '4':
            num_cliente = int(input("Digite o número do cliente: "))
            if num_cliente in cliente_existente:
                att_Cliente_Marca()
                print("Marca alterado com sucesso.")
            else:
                print("Cliente não encontrado.")
        #------Placa------
        elif opcao_menu == '5':
            num_cliente = int(input("Digite o número do cliente: "))
            if num_cliente in cliente_existente:
                att_Cliente_Placa()
                print("Placa alterado com sucesso.")
            else:
                print("Cliente não encontrado.")
        #------Cor------
        elif opcao_menu == '6':
            num_cliente = int(input("Digite o número do cliente: "))
            if num_cliente in cliente_existente:
                att_Cliente_Cor()
                print("Cor alterado com sucesso.")
            else:
                print("Cliente não encontrado.")
        else:
            print("Opção invalida.") 
    else:
        print("Opção invalida.") 
