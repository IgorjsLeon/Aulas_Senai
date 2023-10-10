#Crie um programa que o usuario insira um valor e o programa verificará quantos números pares e impares tem de 1~(nº inserido).
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
