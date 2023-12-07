import os

#Exemplo 1: Obter o diretorio de trabalho atual:

diretorio_atual = os.getcwd()
print(f"O diretorio atual é: {diretorio_atual}")

#Exemplo 2: Listar os arquivos em um diretorio

lista_arquivos = "A:\\Prof. Cassio de Albuquerque\\Python III\\Igor"

arquivos = os.listdir(lista_arquivos)
print(f"Os arquivos do diretorio são: ")
for arquivo in arquivos:
    print(arquivos)

#Exemplo 3: Criar um diretorio

'''nova_diretorio = 'A:\\Prof. Cassio de Albuquerque\\Python III\\Igor'
os.mkdir(nova_diretorio)'''

#Exemplo 4: Executa comandos

os.system('echo Hello, world!')

