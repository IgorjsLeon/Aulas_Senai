#Crie uma função que peça para o usuario digitar o caminho de um diretorio e liste os arquivos de um diretorio utilizando a biblioteca OS
# se digitar .\\ (Você lista o diretorio atual)
import os

def listar_arquivos():
    #Pede um diretorio ao usuario
    diretorio = input("Digite o diretorio desejado: ")
    #Listar os arquivos do diretorio passado
    listar = os.listdir(diretorio)
    for arquivo in listar:
        #Exibe os arquivos do diretorio passado
        print(arquivo)
listar_arquivos()