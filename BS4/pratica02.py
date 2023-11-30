import requests
from bs4 import BeautifulSoup

def pesquisa_preco_amazon():
    produto_pesquisa = input("Digite o produto desejado: ")

    produto_pesquisa = produto_pesquisa.replace(' ', '+')

    url = f'https://www.amazon.com.br/{produto_pesquisa}'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        resultados = soup.find_all('li', class_= 'a-carousel-card acswidget-carousel__card')

        for resultado in resultados[:5]:

            nome_produto = resultado.find('span', class_='a-truncate-cut')
            
            print(f"Nome do produto: {nome_produto}")
    else:
        print(f"A solicitação falhou. Status: {response.status_code}")

pesquisa_preco_amazon()