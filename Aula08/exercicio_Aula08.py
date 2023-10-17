"""pilhas = voce retira os objetos 1 por 1 de cima
fila = primeiro que entra é o primeiro que sai.
def custo_Mercadoria_Vendida(estoque_Inicial, estoque_Final, compras):
    cmv = (estoque_Final + compras - estoque_Inicial)
    print("O estoque atual é de:", cmv)
def valor_Compras_Periodo(estoque_Inicial, estoque_Final):
    valor_Compras_Periodo = (estoque_Final - estoque_Inicial)
    print("O valor compras:", valor_Compras_Periodo)
    """

from funcoes_Clientes import menu_Cliente, inserir_Cliente, inserir_Veiculo, ver_Cliente

while True:
    menu_Cliente()
    opcao_Menu = int(input("Digite a opção desejada(1 ~ 5): "))

    if opcao_Menu == 1:
        cliente = int(input("\nDigite o número do cliente(001 ~ 999): "))
        nome = input("Digite o nome do cliente: ")
        telefone = int(input("Digite o telefone do cliente: "))
        email = input("Digite o e-mail do cliente: ")
        inserir_Cliente(cliente, nome, telefone, email)

    elif opcao_Menu ==2:
        veiculo = int(input("\nDigite o número do veiculo do cliente(001 ~ 999): "))
        marca = input("Digite a marca do carro do cliente: ")
        cor = input("Digite a cor do veiculo do cliente: ")
        placa = input("Digite a placa do veiculo do cliente: ")
        inserir_Veiculo(veiculo, marca, cor, placa)

    elif opcao_Menu == 3:
        ver_Cliente()

    