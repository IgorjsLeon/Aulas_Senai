import sqlite3


#Função para criar uma tabela de contatos

def criar_tabela():
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contatos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT NOT NULL, telefone TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#Funçao para adicionar um novo contato
def adicionar_contato(nome, telefone):
    conn = sqlite3.connect('contatos.db') #Faz a conexão com o banco
    cursor = conn.cursor() #Cria um cursor para escrever no banco
    cursor.execute('''INSERT INTO contatos(nome, telefone) VALUES(?,?)''', (nome, telefone))
    conn.commit()
    conn.close()

#Função para obter dados do contato
def obter_dados():
    conn = sqlite3.connect('contatos.db') #Faz a conexão com o banco
    cursor = conn.cursor() #Cria um cursor para escrever no banco
    cursor.execute('''SELECT * FROM contatos''')
    contatos = cursor.fetchall()
    conn.close()
    return contatos

#Função para atualizar contato
def atualizar_contato(contato_id, novo_nome, novo_telefone):
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE contatos SET nome = ?, telefone = ?, WHERE id = ?''', (novo_nome, novo_telefone, contato_id))
    conn.commit()
    conn.close()

#Função excluir contato
def excluir_contato(contato_id):
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM contato WHERE id=?''', (contato_id))
    conn.commit()
    conn.close()

#Função principal
def main():
    criar_tabela()
    while True:
        print('\nMenu')
        print('1- Adicionar Contatos')
        print('2- Listar Contatos')
        print('3- Atualizar Contatos')
        print('4- Excluir Contatos')
        print('5- Sair')

        opcao = input("Digite a opção desejada: ")
        if opcao =='1':
            nome= input("Digite o nome do contato: ")
            telefone = input('Digite o telefone do contato: ')
            adicionar_contato(nome, telefone)
            print('Contato adicionado com sucesso!')
        elif opcao =='2':
            contatos = obter_dados()
            print('\n Lista de Contatos: ')
            for contato in contatos:
                print(f'{contato[0]}. Nome: {contato[1]}. Telefone: {contato[2]}')
        elif opcao =='3':
            contato_id = input('Digite o Id do contato que deseja atualizar: ')
            novo_nome= input("Digite o novo nome do contato: ")
            novo_telefone= input("Digite o novo número de telefone do contato: ")
            atualizar_contato()
            print("Contato atualizado com sucesso!")
        elif opcao =='4':
            contato_id = input('Digite o Id do contato que deseja excluir: ')
            excluir_contato(contato_id)
            print('Contato excluido com sucesso!')
        elif opcao =='5':
            print('Saindo do programa')
            break
        else:
            print("Opção inválida!")

main()