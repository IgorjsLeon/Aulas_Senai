'''Criar um script com selenium e pyautogui que pesquisa sobre um tema no google, copia e cola o titulo no bloco de notas e o salva'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

def pesquisa_chrome():
    pesquisa = input("O que deseja pesquisar?: ")

    navegador = webdriver.Chrome()

    navegador.get('https://www.google.com.br/')
    time.sleep(2)

    try:
        elemento = navegador.find_element(By.ID, 'APjFqb')
        elemento.send_keys(pesquisa)
        elemento.send_keys(Keys.RETURN)
        elemento1 = navegador.find_element(By.NAME)
        time.sleep(1)
        print(elemento1)
        '''pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.press('winleft')
        pyautogui.write('bloco de notas')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'v')'''

    except:
        print('Erro')

    finally:
        navegador.close()



pesquisa_chrome()