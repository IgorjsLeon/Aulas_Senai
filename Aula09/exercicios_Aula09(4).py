#Crie uma classe Pedido que permite criar objetos que representam pedidos em um restaurante. Cada objeto de pedido deve conter informações como Nome do cliente, item do pedido, valor total.

class Pedido:
    def __init__(self, nome_Cliente, itens ,valor_Total):
        self.nome_Cliente = nome_Cliente
        self.itens = itens
        self.valor_Total = valor_Total

pedido1 = Pedido('Igor', 'Filé de frango', 25.50)