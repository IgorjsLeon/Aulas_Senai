import pandas as pd
import matplotlib.pyplot as plt

# Criação de um DataFrame
# Passo 1: Dados fictícios
dados_alunos = {
    'Nome': ['João', 'Maria', 'Carlos', 'Ana'],
    'Idade': [18, 20, 19, 22],
    'Nota_Matematica': [90, 85, 88, 92],
    'Nota_Portugues': [78, 80, 75, 85]
}

# Passo 2: Criar o DataFrame
df_alunos = pd.DataFrame(dados_alunos)

# Passo 3: Exibir o DataFrame
print(df_alunos)

# Análise de Dados:

# Média das notas de Matemática
media_matematica = df_alunos['Nota_Matematica'].mean()
media_portugues = df_alunos['Nota_Portugues'].mean()

# Imprimir a média
print(f"Média em Matemática: {media_matematica}.")
print(f"Média de Português: {media_portugues}.")

###############

#Visualização de Dados:

#Gráfico de Barra das notas de Matemática

df_alunos.plot( x = 'Nome', y=['Nota_Matematica', 'Nota_Portugues'], kind='bar')

plt.title("Notas dos Alunos em Matematica e Portugues")

plt.xlabel("Aluno")
plt.ylabel("Nota")
plt.show()




