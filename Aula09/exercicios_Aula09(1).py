#Criar uma classe calculadora que possui metodos para adicionar, subtrair, multiplicar e dividir dois numeros.

#-------------------Criando a classe calculadora-------------------

class Calculadora:
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2

#-------------------Criando a função somar-------------------

    def somar(self, num1, num2):
        return num1 + num2

    #-------------------Criando a função subtrair-------------------

    def sub(self, num1, num2):
        return num1 - num2

    #-------------------Criando a função multiplicar-------------------

    def mult(self, num1, num2):
        return num1 * num2

    #-------------------Criando a função dividir-------------------

    def div(self, num1, num2):
        return num1 / num2


