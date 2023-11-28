#coloque pip install selenium
#coloque pip install by
from selenium import webdriver
import time
from selenium.webdriver.common.by import By #importando o by
from selenium.webdriver.common.keys import Keys

#Instanciar um navegador (Chrome, firefox e etc)

navegador = webdriver.Chrome()

#Navegar utilizando o selenium

navegador.get('https://www.google.com.br/')

try: #Encapsula um código que pode gerar erro.
    #Encontrar um elemento pelo ID

    elemento = navegador.find_element(By.ID,'APjFqb')

    #Digita um texto no campo selecionado

    elemento.send_keys("greve de metro em São Paulo")

    #Simula a tecla enter

    elemento.send_keys(Keys.RETURN)

    time.sleep(5) #Aguarda 5 segundos

except:
    print('Erro')
    

finally:
    navegador.close()