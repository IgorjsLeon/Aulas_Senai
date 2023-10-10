print("###########################################################################")
print("#                                                                         #")
print("#    1 - Exercicio 1 (Intercalamento de frases)                           #")
print("#    2 - Exercicio 2 (Frase sai tudo maiusculo, minusculo e em lista)     #")
print("#    3 - Exercicio 3 (Sorteio de um número)                               #")
print("#    4 - Exercicio 4 (Calculadora)                                        #")
print("#    5 - Exercicio 5 (Contagem de números pares e impares)                #")
print("#                                                                         #")
print("###########################################################################")

escolha_Exer = int(input("Digite o valor do exercicio (1~5): "))

#(Exercicio 1) - Crie uma frase com três variaveis numericas e intercalem essas variaves no seu texto
if escolha_Exer == 1:
    frase_2 = "essa"
    frase_1 = "Meia noite eu te conto o porquê"
    frase = "frase não faz sentido"
    print(f"\nSabemos que {frase_1} {frase_2} {frase}\n")

#(Exercicio 2) - Elabore um programa que o usuario digite uma frase e o programa devolva a frase com todas as letras maiusculas, minusculas e em forma de lista
elif escolha_Exer == 2:
    frase = input("\nDigite uma frase: ")
    print(frase.upper())
    print(frase.lower())
    print(frase.split(),"\n")

    """ while ( condição ), ex
    numero = 0
    while ( numero < 10):
    print(numero)
    numero += 1 (+= significa que "numero = numero + 1)"""

#(Exercicio 3) - Elabore um programa que o usuario tem que adivinhar um numero e caso ele erre, o programa da uma dica. 
elif escolha_Exer == 3:
    import random
    num_Sorteado = random.randint (1, 100)
    sorteio = True
    while (sorteio == True):
        palpite = int(input("\nAcerte o número sorteado de 1 ~ 100: "))
        if palpite == num_Sorteado:
            print(f"Parabêns você acertou! O número sorteado era {num_Sorteado}!\n")
            sorteio = False
        elif (palpite > num_Sorteado):
            print("Tente um número menor")
        else:
            print("Tente um número maior")

#(Exercicio 4) - Elabore uma calculadora, pedindo pro usuario digitar um numero 1 e um numero 2 e ele escolhe a opção das operações e um botao para sair. 
elif escolha_Exer == 4:
    print("\n#####################################")
    print("#                                   #")
    print("# Bem-vindo à calculadora em Python #")
    print("#          by Igor Leon             #")
    print("#                                   #")
    print("#####################################")
    print("--------------------------------")
    print("-       1 - Adição             -")
    print("-       2 - Subtração          -")
    print("-       3 - Multiplicação      -")
    print("-       4 - Divisão            -")
    print("--------------------------------")
    calculadora = True
    escolha_Calc = int(input("Qual operação você gostaria de utilizar?(1~4): "))
    while (calculadora == True):
        if escolha_Calc == 1:
            num_1 = float(input("Digite o primeiro número: "))
            num_2 = float(input("Digite o segundo número: "))
            soma = num_1 + num_2
            print(f"A soma de {num_1} e {num_2} é {soma}.")
            print("Deseja fechar o programa ou escolher outra operação?")
            retorno = input("Digite fechar: ")
            if retorno == "fechar":
                print("Obrigado por utilizar o meu programa!")
                calculadora = False
        elif escolha_Calc == 2:
            num_1 = float(input("Digite o primeiro número: "))
            num_2 = float(input("Digite o segundo número: "))
            sub = num_1 - num_2
            print(f"A subtração de {num_1} e {num_2} é {sub}.")
            print("Deseja fechar o programa ou escolher outra operação?")
            retorno = input("Digite fechar: ")
            if retorno == "fechar":
                print("Obrigado por utilizar o meu programa!")
                calculadora = False
        elif escolha_Calc == 3:
            num_1 = float(input("Digite o primeiro número: "))
            num_2 = float(input("Digite o segundo número: "))
            mult = num_1 * num_2
            print(f"A multiplicação de {num_1} e {num_2} é {mult}.")
            print("Deseja fechar o programa ou escolher outra operação?")
            retorno = input("Digite fechar: ")
            if retorno == "fechar":
                print("Obrigado por utilizar o meu programa!")
                calculadora = False
        elif escolha_Calc == 4:
            num_1 = float(input("Digite o primeiro número: "))
            num_2 = float(input("Digite o segundo número: "))
            div = num_1 / num_2
            print(f"A divisão de {num_1} e {num_2} é {div}.")
            print("Deseja fechar o programa ou escolher outra operação?")
            retorno = input("Digite fechar: ")
            if retorno == "fechar":
                print("Obrigado por utilizar o meu programa!")
                calculadora = False

#(Exercicio 5) - Pedir pro usuario digitar um número e o programa diz quantos números são pares e impares até o valor digitado.

elif escolha_Exer == 5:
    numero_digitado = int(input("Digite um número inteiro: "))
    pares = 0
    impares = 0
    for i in range(1, numero_digitado + 1):
        if i % 2 == 0:
            # Se o número for par, incrementa a contagem de números pares
            pares += 1 
        else:
            # Se o número for ímpar, incrementa a contagem de números ímpares
            impares += 1
    print(f"Entre 1 e {numero_digitado}, há {pares} número(s) par(es) e {impares} número(s) ímpar(es).")