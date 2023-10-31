class Shape:
    def calcular_area(self):
        pass

class Circulo(Shape):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self, raio):
        area = raio * raio * 3.14
        return f'A área do circulo é {area}'
    
class Retangulo(Shape):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self, base, altura):
        area = base * altura
        return f'A área do retangulo é {area}'
    
while True:
    opcao = input("Deseja calcular a área do circulo ou retangulo?(c / r): ")

    if opcao == 'c':
        raio = float(input("Digite o valor do Raio: "))
        circulo = Circulo(raio)
        print(circulo.calcular_area(raio))
    elif opcao == 'r':
        base = float(input("Digite o valor da Base: "))
        altura = float(input("Digite o valor da Altura: "))
        retangulo = Retangulo(base, altura)
        print(retangulo.calcular_area(base, altura))
    else:
        print("Opção inválida!")


