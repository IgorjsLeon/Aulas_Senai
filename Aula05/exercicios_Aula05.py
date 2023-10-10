"""lista = [], uma lista guarda diversas variaveis e nela você pode guardar qualquer tipo de valor, pode usar números, nomes e etc.
metodos de lista:
    lista.append() - ele adiciona um elemento no final da lista
    lista.sort() - ele coloca em ordem alfabetica ou em ordem crescente numerica
    Para exibir um determinado elemento da lista vc coloca print(lista[numero que deseja saber na lista (ele puxa o indice da sua lista)])
    exemplo de indice:
indice:  0  1  2  3  4  5
lista = [1, 2, 3, 4, 5, 6]. Ou seja, se você der print(lista[5]) ele te retornará o valor "4".
        COMANDO for:
        for i in lista:
        print(i) - printa o valor das listas(ele faz uma busca e exibe os valores, você pode utilizar varios if's para filtrar os dados da sua lista e ir organizando os dados da melhor maneira).
        temos tambem o for i in range(1, 10, 3): - (1) seria o valor inicial (10) seria o valor final a ser exibido (3) o programa vai imprimir de 3 em 3 (Exemplo: 1, 4, 7, 10).
        print(i) - o range é um intervalo
    Para somar elementos de uma lista:
    numero = [1, 2, 3, 4]
     soma = sum(numero)
      print(soma) """


print("###########################################################################")
print("#                                                                         #")
print("#    1 - Exercicio 1 (Crie e some uma lista)                              #")
print("#    2 - Exercicio 2 (Imprimindo valor max, min e forma ordenada)         #")
print("#    3 - Exercicio 3 (Lista de tarefas)                                   #")
print("#    4 - Exercicio 4 (Lista de tarefas que mostra a média)                #")
print("#                                                                         #")
print("###########################################################################")

escolha_Exer = int(input("Digite o valor do exercicio (): "))

#(Exercicio 1) - Crie uma lista qualquer e some os elementos dessa lista.

if escolha_Exer == 1: #Escolha do exercicio
    num = [1, 2, 100, 40, 10, 30, 45, 50, 3, 4, 5]
    soma = sum(num)
    print(f"A soma da sua lista é {soma}")

#(Exercicio 2) - Dentro da lista de números acima imprima o valor max e o valor min e coloque na forma ordenada.

elif escolha_Exer == 2: #Escolha do exercicio
    num = [1, 2, 100, 40, 10, 30, 45, 50, 3, 4, 5]
    # Max e min
    maximo = max(num)
    minimo = min(num)
    print(f"O valor maximo é {maximo} e o valor minimo é {minimo}")
    #Colocar em forma ordenada
    num.sort()
    print(f"A forma ordenada é: {num}")

#(Exercicio 3) - Crie um programa que simule uma lista de tarefas. Crie um menu que insira, exclua, ordene tarefas nesta lista e conte a quantidade de tarefas.

elif escolha_Exer == 3: #Escolha do exercicio
    menu = True  # Habilita o menu.
    lista_Tarefas = []  # Cria a lista de tarefas que o usuário irá preencher.

    while menu:
        print("#############################################")
        print("#                                           #")
        print("# Bem-vindo(a) Lista de tarefas em Python   #")
        print("#               By: Igor Leon               #")
        print("#                                           #")
        print("# Opção 01 - Adicionar elementos na lista   #")
        print("# Opção 02 - Exclua elementos da lista      #")
        print("# Opção 03 - Listar tarefas                 #")
        print("# Opção 04 - Sair do programa               #")
        print("#                                           #")
        print("#############################################\n")
        
        opcao = input("Digite qual opção deseja realizar (1~4): ")
        
        if opcao == "1":
            while True:
                print(lista_Tarefas)
                tarefa = input("\nDigite a tarefa: ")
                lista_Tarefas.append(tarefa)
                voltar_ao_Menu = input("Deseja voltar ao menu? (s / n): ")
                if voltar_ao_Menu != "n":
                    break

        elif opcao == "2":
            for index, ver_Tarefas in enumerate(lista_Tarefas):
                print(f"{index}: {ver_Tarefas}")
            excluir = input("Qual tarefa deseja excluir: ")
            try:
                index = int(excluir)
                if 0 <= index < len(lista_Tarefas):
                    del lista_Tarefas[index]
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, insira um número válido.")
            
        elif opcao == "3":
            while True:
                for tarefa in lista_Tarefas:
                    print(tarefa)
                voltar_ao_Menu = input("Deseja voltar ao menu? (s / n): ")
                if voltar_ao_Menu != "n":
                    break
        elif opcao == "4":
            print("Obrigado por utilizar o programa")
            menu = False
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")



#(Exercicio 4) - Crie um programa que o usuario digite valores e depois tire a média da lista.

elif escolha_Exer == 4: #Escolha do exercicio
    numero_Usuario = []
    quantidade_Num = 0
    menu = True
    while menu == True:
        print("----------------------")
        print("- 1 - insira o valor -")
        print("- 2 - Tire a média   -")
        print("----------------------")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1: #Desidi colocar para que a lista armazene apenas 10 valores.
            if quantidade_Num < 10:
                while True:
                    num = float(input("Digite o valor desejado: "))
                    numero_Usuario.append(num)
                    quantidade_Num += 1
                    retornar = input("Deseja retornar ao menu?(s / n): ")
                    if quantidade_Num == 10:
                        print("Sua lista já esta no limite.")
                        break
                    elif retornar != "n":
                        break
            else:
                print("Você ja atingiu o valor máximo permitido.")
        elif opcao == 2: #Média da lista.
            soma = sum(numero_Usuario)
            media = soma / quantidade_Num
            print(f"Sua média é : {media}")
            menu = False
        else:
            print("Opção invalida.")
