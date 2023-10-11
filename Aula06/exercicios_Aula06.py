while True:
    print("-----------------------------------------")
    print("-                                       -")
    print("- 1- Exercício (Dicionario de contatos) -")
    print("- 2- Exercício (Dicionario manual)      -")
    print("- 3- Exercício (Dicionario com Menu)    -")
    print("-                                       -")
    print("-----------------------------------------")

    escolha_Exercicios = int(input("Digite qual exercício deseja acessar(1~3): "))

#(Exercício 1)- Crie uma lista chamado "agenda" com dicíonarios de nome, telefone, e-mail e endereço
    
    if (escolha_Exercicios == 1):
        print("---------------")
        print("- Exercício 1 -")
        print("---------------")
        agenda = [{"Nome": "Igor", "Telefone": 123456789, "E-mail": "igor@igor", "Endereço": "Av. Sapopemba, 13300"},
              {"Nome": "Joelma", "Telefone": 987654321, "E-mail": "joelma@joelma", "Endereço": "Av. Sapopemba, 13300"}, 
              {"Nome": "Cássio", "Telefone": 246897531, "E-mail": "cassio@cassio", "Endereço": "Rua Secundino Domingues, 22"},
              {"Nome": "Leonardo", "Telefone": 465879541, "E-mail": "leo@leo", "Endereço": "Rua das figueiras, 3500"},
              {"Nome": "Amanda", "Telefone": 852456321, "E-mail": "amanda@amanda", "Endereço": "Rua 13 de julho, 1500 "}]
        for i in agenda:
            print(i, "\n")
        #---------------Retorno ao menu de exercícios--------------
        retorno_Menu = input("Deseja retornar ao menu de exercícios?(s/n): ")
        if (retorno_Menu != "s"):
            break
    
#(Exercício 2)- Crie uma lista chamado "agenda" com dicíonarios de nome, telefone, e-mail e endereço, sendo que o usuario digite os valores.

    elif (escolha_Exercicios == 2):
        print("---------------")
        print("- Exercício 2 -")
        print("---------------")
        agenda = [{"Nome": input("Digite seu nome: "), "Telefone": int(input("Digite seu telefone: ")), "E-mail": input("Digite o seu e-mail: "), "Endereço": input("Digite o seu endereço: ")},
                  {"Nome": input("Digite seu nome: "), "Telefone": int(input("Digite seu telefone: ")), "E-mail": input("Digite o seu e-mail: "), "Endereço": input("Digite o seu endereço: ")},
                  {"Nome": input("Digite seu nome: "), "Telefone": int(input("Digite seu telefone: ")), "E-mail": input("Digite o seu e-mail: "), "Endereço": input("Digite o seu endereço: ")},
                  {"Nome": input("Digite seu nome: "), "Telefone": int(input("Digite seu telefone: ")), "E-mail": input("Digite o seu e-mail: "), "Endereço": input("Digite o seu endereço: ")},
                  {"Nome": input("Digite seu nome: "), "Telefone": int(input("Digite seu telefone: ")), "E-mail": input("Digite o seu e-mail: "), "Endereço": input("Digite o seu endereço: ")}]
        for i in agenda:
            print(i, "\n")
        #---------------Retorno ao menu de exercícios--------------
        retorno_Menu = input("Deseja retornar ao menu de exercícios?(s/n): ")
        if (retorno_Menu != "s"):
            break

#(Exercício 3)- Crie uma lista chamado "agenda" com dicíonarios de nome e telefone, sendo que o usuario escolhe entre add contatos e verificar os dicionarios.

    elif (escolha_Exercicios == 3):
        print("---------------")
        print("- Exercício 3 -")
        print("---------------")
        agenda = []

        while True:
            print("\n--------------------------")
            print("- 1 - Adicionar Contatos -")
            print("- 2 - Verificar Contatos -")
            print("- 3 - Sair               -")
            print("--------------------------")
            
            escolhas_Menu = int(input("Digite qual opção você deseja utilizar (1 ~ 3): "))
            
            while escolhas_Menu == 1:
                agenda.append({"Nome": input("Digite o nome: "), "Telefone": int(input("Digite o telefone: "))})
                voltar = input("Deseja voltar ao menu? (s/n): ")
                if voltar != "n":
                    break
            
            if escolhas_Menu == 2:
                print("\n-----------------------------------------------------")
                print("- 1 - Ver todos os Contatos                         -")
                print("- 2 - Verificar Nome do Contato através do telefone -")
                print("- 3 - Verificar Telefone do Contato através do nome -")
                print("-----------------------------------------------------")
                
                escolhas_Menu = int(input("Digite qual opção você deseja utilizar (1 ~ 3): "))
                
                if escolhas_Menu == 1:
                    for contato in agenda:
                        print("Nome:", contato["Nome"])
                        print("Telefone:", contato["Telefone"])
                
                elif escolhas_Menu == 2:
                    telefone = int(input("\nDigite o telefone do contato que deseja encontrar: "))
                    for contato in agenda:
                        if contato["Telefone"] == telefone:
                            print("Nome do Contato:", contato["Nome"])
                
                elif escolhas_Menu == 3:
                    nome = input("\nDigite o nome do contato que deseja encontrar: ")
                    for contato in agenda:
                        if contato["Nome"] == nome:
                            print("Telefone do Contato:", contato["Telefone"])
            
            elif escolhas_Menu == 3:
                break
