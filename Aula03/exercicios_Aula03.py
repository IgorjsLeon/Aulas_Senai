#---------------------Escolha qual exercicio quer executar------------------------

escolha_Exercicio = int(input("Digite 1 à 5 para selecionar o exercicio: "))

#------(Exercicio 1)--------------------usuario digita um número e verifica se o número é positivo, negativo ou zero

if escolha_Exercicio == 1:
    numero = int(input("\nDigite um numero: "))
    if (numero == 0):
        print("\nÉ igual a zero")
    elif (numero < 0):
        print("\nÉ um número negativo")
    elif (numero > 0):
        print("\nÉ um número positivo")
    else:
        print("\nChama o professor")

#-----(Exercicio 2)------------------Verifique a idade de uma pessoa, informe a ela se o voto dela é facultativo (>= 16 e < 18 e < 65) ou obrigatorio (18 até 65)

if escolha_Exercicio == 2:
    idade = int(input("Digite sua idade: "))
    if (idade < 16):
        print("\nNão pode votar")
    elif (idade >= 16 and idade < 18):
        print("\nSeu voto é facultativo")
    elif (idade >= 18 and idade <= 65):
        print("\nSeu voto é obrigatorio")
    elif (idade > 65 ):
        print("\nSeu voto é facultativo")
    else:
        print("\nChama o professor")

#------(Exercicio 3)--------------------Escreva um programa que pessa para o usuario digitar 3 numero e verifique qual é o maior deles.

if escolha_Exercicio == 3:
    numero_1 = float(input("\nDigite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    numero_3 = float(input("Digite o terceiro número: "))
    if (numero_1 > numero_2 and numero_1 > numero_3):
        print("\nO primeiro número é maior que todos os outros.")
    elif (numero_2 > numero_1 and numero_2 > numero_3):
        print("\nO segundo número é maior que todos os outros.") 
    elif (numero_3 > numero_1 and numero_3 > numero_2):
        print("\nO terceiro número é maior que todos os outros.")
    else:
        print("\nchamar o professor.")       

#------(Exercicio 4)--------------------Escreva um programa que informe se um número é par ou impar.

if escolha_Exercicio == 4:
    numero = int(input("Digite um número inteiro: "))
    d = numero % 2
    if (d == 0):
        print("\nEste número é par.")
    else:
        print("\nEste número é impar.")

#------(Exercicio 5)--------------------Escreva um dia da semana se for sabado ou domingo (Final de semana) se não dia da semana

if escolha_Exercicio == 5:
    dia_Semana = input("Digite qual dia da semana você quer: ") #Comando input já tem a função "str".
    if (dia_Semana == "sabado" or dia_Semana == "domingo"):
        print("\nFinal de semana.")
    else:
        print("\nDia util.")