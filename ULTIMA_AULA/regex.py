import re

#Funções Básicas
# "re.search()" : Procura pela primeira ocorrencia do padrão de String

texto = "Python é uma linguagem de programação poderosa. Ela serve para fazer vários tipos de automação de tarefas maçantes"
padrao = r"Python"
resultado = re.search(padrao, texto)
print(resultado.group()) # saida 

#b 're.findall()' :Encontra todas as ocorrencias do padrão de String
texto = "Python é uma linguagem de programação poderosa. Ela serve para fazer vários tipos de automação de tarefas maçantes"
padrao = r"o"
resultado = re.findall(padrao, texto)
print (resultado)# saida 


#Substituir um padrão: 
# 're.sub()'

texto = "Python é uma linguagem de programação poderosa. Ela serve para fazer vários tipos de automação de tarefas maçantes"

padrao = r"Python"
substituicao = "Java"
novo_texto = re.sub(padrao, substituicao, texto)
print(novo_texto) # saída do novo texto

