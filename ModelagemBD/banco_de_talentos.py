import mysql.connector

conn = mysql.connector.connect(
    nome = 'localhost',
    user = 'root',
    password = 'senai',
    database = 'banco_de_talentos'
)
cursor = conn.cursor()

#inserir cliente
def inserir_candidato(cpf, nome, email, linkdl, github):
    querry = 'INSERT INTO candidato (cpf, nome, email, linkdl, github) VALUES (%s, %s, %s, %s, %s)'
    values = (cpf, nome, email, linkdl, github)
    cursor.execute(querry, values)
    conn.commit()


while True:
    print("Bem-vindo(a) ao Bando de Talentos")
    print("           by Igor Leon          ")
    print("      1-Incluir Candidato        ")
    print("      2-Listar Candidato         ")
    print("      3-Atualizar Candidato      ")
    print("      4-Deletar Cadidato         ")

    opcao = input("Digite a opção desejada(1 ~ 4): ")

    if opcao == '1':
        try:
            cpf = int(input("Digite o CPF do candidato: "))
        except:
            print("O CPF deve conter apenas números")
        nome = input("Digite o Nome Completo do candidato: ")
        email = input("Digite o E-mail do candidato: ")
        linkdl = input("Digite o Linkdl do candidato: ")
        github = input("Digite o Github do candidato: ")
        inserir_candidato(cpf, nome, email, linkdl, github)
    else:
        print("Opção inválida!")
