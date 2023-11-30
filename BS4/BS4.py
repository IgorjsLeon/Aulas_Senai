#Instalar a Biblioteca BS4: pip install bs4
#Instalar os requests: pip install requests
#importar a biblioteca BS4

from bs4 import BeautifulSoup
import requests

#URL da pagina web a ser rapada

url = 'https://www.mercadolivre.com.br/gabinete-gamer-tgt-jester-lateral-vidro-com-2-fans-micro-atx/p/MLB22301121#polycard_client=recommendations_home_navigation-recommendations&reco_backend=machinalis-homes-pdp-boos&reco_client=home_navigation-recommendations&reco_item_pos=0&reco_backend_type=function&reco_id=8a9ec2d2-2114-4133-8ee6-cf70c01daedd&wid=MLB3402387283&sid=recos'

#Enviar uma solicitação GET para a página

response = requests.get(url)

#Verifica se solicitação foi bem sucedida

if response.status_code == 200:
    #Criar um objeto BeautfulSoup para analisar o nosso conteúdo HTML da página

    soup = BeautifulSoup(response.text, 'html.parser')

    #Procura o primeiro elemento H1

    h1 = soup.find('h1')

    #Exibir o texto dentro da TAG H1

    print(f'Titulo da Página:{h1.text}\n')

    #Exibir todos os elementos HTML correspondentes a uma tag especifica

    todos_links = soup.find_all('a')

    #Exibir os URL's de todos os links da página

    for link in todos_links:
        print(link.get('href'))

    #Acessar atributos de um elemento HTML

    img_src = soup.find('img')['src']
    print(img_src)

    #Navegar pela arvore DOM, navegar pelo HTML para encontrar elementos alinhados

    conteudo_div = soup.find('div', class_='ui-pdp-header__title-container')
    conteudo_spam = soup.find('spam', class_='andes-visually-hidden')
    print(conteudo_div)

    #Exibir o texto dentro da TAG <div class= 'conteudo'>

    print('Conteudo da Div: ')
    print(conteudo_div.text.strip())
    print('Conteudo do Preço: ') 
    print(conteudo_spam.text.strip())

    #Encontrar todos os elementos de uma classe especifica

    todos_elementos_classe_x = soup.find_all(class_= 'ui-search-item__brand-discoverability ui-search-item__group__element')

    #Exibir os elementos da classe

    print('Elementos da Classe: ')
    print(todos_elementos_classe_x.text.strip())

    #Encontrar o proximo elemento irmão

    elemento_filho = title_tag.find_next_sibling()

    #Encontrar elementos pelo seletor CSS

    elemento_css = soup.select('.minha-classe_css')

else:
    print(f'A solicitação falhou com o código de status{response.status_code}')