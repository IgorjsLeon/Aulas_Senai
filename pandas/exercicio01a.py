import pandas as pd
import matplotlib.pyplot as plt

#Lista de vendedores

ranking_vendas ={
    "Vendedor":["João","Marcelo", "Paula","Felipe", "Thais"],
    "Valor_Vendido":[10000.00, 5000.00,7800.00,5800.00, 6000.00],
    "Coversao_Vendas":[2000, 3000,1000,5000, 5800]
}

#Criar seu dataframe
df = pd.DataFrame(ranking_vendas)
print(df)

media_vendas = df['Valor_Vendido'].mean()
media_conversao= df['Coversao_Vendas'].mean()
maximo_venda= df['Valor_Vendido'].max()
minimo_venda= df['Valor_Vendido'].min()

print(f"Média de Venda: {media_vendas}")
print(f"Média de Conversao:{media_conversao}")
print(f"Maior valor vendido: {maximo_venda}")
print(f"Menor valor vendido: {minimo_venda}")

#Visualização de Dados:

#Gráfico de Barra 

df.plot(x='Vendedor', y=['Valor_Vendido', 'Coversao_Vendas'], kind="bar")


plt.title("Ranking Vendedores")

plt.xlabel("Vendedor")
plt.ylabel("Resultado")
plt.show()


