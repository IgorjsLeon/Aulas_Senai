#Conectar ao banco de dados (lembrando que precisa usar 'pip install mysql-connector-python', )

import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'senai', 
    database = 'loja_ii'
    )
cursor = conn.cursor()

#Script para criar uma tabela chamada cliente_vip

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente_vip(
               idcliente INT AUTO_INCREMENT PRIMARY KEY,
               nome VARCHAR(45) NOT NULL,
               endereco VARCHAR(255) NOT NULL,
               telefone INT(13),
               email VARCHAR(45) NOT NULL,
               cpf INT(20) NOT NULL
                )''')

#Função para inserir dados na tabela cliente

def inserir_cliente(nome, endereco, telefone, email, cpf):
    query = 'INSERT INTO cliente_vip (nome, endereco, telefone, email, cpf) VALUES (%s, %s, %s, %s, %s)'
    values = (nome, endereco, telefone, email, cpf)
    cursor.execute(query, values)
    conn.commit()

#Função para listar todos os clientes

def listar_cliente():
    cursor.execute('SELECT * FROM cliente_vip')
    cliente = cursor.fetchall()
    for clientes in cliente:
        print(clientes)

#Função para atualizar a tabela cliente_vip

def atualizar_cliente_vip(idcliente, nome, endereco, telefone, email, cpf):
    query = 'UPDATE cliente_vip SET nome = %s, endereco = %s, telefone = %s, email = %s, cpf = %s WHERE idcliente = %s'
    values = (idcliente, nome, endereco, telefone, email, cpf)
    cursor.execute(query, values)

#Função para deletar um cliente

def delete_cliente(idcliente):
    query = 'DELETE FROM cliente_vip WHERE idcliente = %s'
    values = (idcliente,)
    cursor.execute(query, values)
    conn.commit()

#Exemplo de uso:

#inserir_cliente('Igor Leon', 'rua do Batman', '123456789', 'igor@igor', '987654321')
delete_cliente(2)


#Crie um sistema para adicionar curriculuns
#Crie um banco de dados chamado "Banco de Talentos"

#Este sistema deverá ter as tabelas

#candidato: (nome, email, cpf, linkdl, github)

#formação: (escolaridade, instituição, curso, duração)

#experiencia profissional: (empresa, cargo, tempo)

#opções para o programa: (incluir candidato, atualizar candidato, deletar cadidato, listar candidato)
