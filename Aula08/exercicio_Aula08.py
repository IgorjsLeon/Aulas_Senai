"""pilhas = voce retira os objetos 1 por 1 de cima
fila = primeiro que entra é o primeiro que sai.
def custo_Mercadoria_Vendida(estoque_Inicial, estoque_Final, compras):
    cmv = (estoque_Final + compras - estoque_Inicial)
    print("O estoque atual é de:", cmv)
def valor_Compras_Periodo(estoque_Inicial, estoque_Final):
    valor_Compras_Periodo = (estoque_Final - estoque_Inicial)
    print("O valor compras:", valor_Compras_Periodo)
    """

from funcoes_Clientes import menu_Cliente, ver_Cliente, inserir_Clienteveiculo, att_Cliente_Nome, menu_Att, att_Cliente_Telefone, att_Cliente_Email , att_Cliente_Marca, att_Cliente_Cor, att_Cliente_Placa
lista_Cliente = []
numeros_clientes_inseridos = set()
while True:
    menu_Cliente()
    opcao_Menu = int(input("Digite a opção desejada(1 ~ 5): "))

    if opcao_Menu == 1:
        num_Cliente = int(input("\nDigite o número do cliente(1 ~ ...): "))
        if num_Cliente not in numeros_clientes_inseridos:
            nome = input("Digite o nome do cliente: ")
            telefone = int(input("Digite o telefone do cliente: "))
            email = input("Digite o e-mail do cliente: ")
            marca = input("Digite a marca do carro do cliente: ")
            cor = input("Digite a cor do veiculo do cliente: ")
            placa = input("Digite a placa do veiculo do cliente: ")
            inserir_Clienteveiculo(num_Cliente, nome, telefone, email, marca, cor, placa)

            # Adicione o número do cliente ao conjunto
            numeros_clientes_inseridos.add(num_Cliente)
        else:
            print("Este cliente ja existe, caso queira atualizar use a função número 3.")
    elif opcao_Menu == 2:
        ver_Cliente()
    elif opcao_Menu == 3:
        num_Cliente = int(input("Digite o número do cliente: "))
        cliente = None  # Inicialize como None
        for c in lista_Cliente:
            if c['Numero Cliente'] == num_Cliente:
                cliente = True  # Encontrou o cliente
                break
        if cliente == True:
            menu_Att()
            opcao_Att = int(input("Digite a opção desejada: "))
            if opcao_Att == 1:
                att_Cliente_Nome(cliente)
            elif opcao_Att == 2:
                att_Cliente_Telefone(cliente)
            elif opcao_Att == 3:
                att_Cliente_Email(cliente)
            elif opcao_Att == 4:
                att_Cliente_Marca(cliente)
            elif opcao_Att == 5:
                att_Cliente_Cor(cliente)
            elif opcao_Att == 6:
                att_Cliente_Placa(cliente)
        else:
            print("Cliente não encontrado.")
