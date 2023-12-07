#Crie uma função que cria um diretorio e pergunte ao usuario qual sera o nome
import os

def criar_diretorio():
    novo_diretorio = input("Digite qual o diretorio deseja criar: ")
    os.mkdir(novo_diretorio)
    print(f'O diretorio {novo_diretorio} foi criado com sucesso.')

criar_diretorio()

