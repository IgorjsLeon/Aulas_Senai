import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from operator import itemgetter
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt
import time  

# Declare global variable
preco = 0.0
lista_produtos = []

def pesquisar_no_mercado_livre():
    global preco
    global lista_produtos 

    navegador = webdriver.Chrome()

    navegador.get('https://www.mercadolivre.com.br/')

    sleep(2)

    pesquisa = entrada_txt.get()

    input_place = navegador.find_element(By.TAG_NAME, "input")
    input_place.send_keys(pesquisa)
    input_place.submit()

    page_content = navegador.page_source
    time.sleep(2)  # Add this line to give the page time to load
    site = BeautifulSoup(page_content, 'html.parser')

    flag_pagina_seguinte = True

    while flag_pagina_seguinte == True:
        produtos = site.findAll('div', attrs={'class': 'ui-search-result'})

        for produto in produtos:
            h_ref = produto.find('a')
            preco = produto.find('span', attrs={'aria-roledescription': 'Preço'}).contents[1].text
            preco = preco.replace('.', '')
            preco = preco.replace(',', '.')
            preco = float(preco)

            lista_produtos.append([h_ref['title'], "{:.2f}".format(preco), h_ref['href'], preco])
        try:
            btn_seguinte = navegador.find_element(By.XPATH, value="//a[@title='Seguinte']")
            navegador.execute_script("arguments[0].click();", btn_seguinte)
            sleep(3)
        except:
            flag_pagina_seguinte = False
            pass

    lista_ordenada = sorted(lista_produtos, key=itemgetter(3))

    for item in lista_ordenada:
        del item[3]

    arq_produtos = pd.DataFrame(lista_ordenada, columns=['Título', 'Preço', 'Link'])
    arq_produtos.to_excel(f'{pesquisa}.xlsx', index=False)

def graficos():
    df_dados = pd.DataFrame(lista_produtos, columns=['Título', 'Preço', 'Link'])
    df_dados['Valor'] = df_dados['Preço'].apply(lambda x: float(x.replace(',', '.')))
    media_preco = df_dados['Valor'].mean()
    
    # Cria uma figura e eixo separadamente
    fig, ax = plt.subplots()
    
    # Usa barh diretamente no eixo para ter controle sobre as configurações
    bars = ax.barh([entrada_txt.get()], [media_preco])
    
    # Define o título e rótulos dos eixos
    plt.title(f'Valor médio de {entrada_txt.get()}')
    plt.xlabel('Valor')
    plt.ylabel('Nome Produto')
    
    # Adiciona o texto da média nas barras
    for bar in bars:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'Média: {media_preco:.2f}', 
                va='center', color='red')
    
    plt.show()


janela = tk.Tk()
janela.geometry("500x500+800+200")

label = tk.Label(janela, text='Produto')
label.pack()

entrada_txt = tk.Entry(janela, width=10)
entrada_txt.pack()

botao = tk.Button(janela, text='Procurar', command=pesquisar_no_mercado_livre)
botao.pack()

botao_dados = tk.Button(janela, text='Dados', command=graficos)
botao_dados.pack()

janela.mainloop()
