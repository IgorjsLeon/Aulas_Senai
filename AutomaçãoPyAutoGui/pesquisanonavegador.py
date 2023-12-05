import pyautogui
import time

def pesquisa_navegador():
    #Pede um input do usuario

    pesquisa = input("Digite a URL do site desejado: ")
    time.sleep(1)

    #Abre o navegador

    pyautogui.press('winleft')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(2)

    #Digita a pesquisa do usuario

    pyautogui.write(pesquisa)
    pyautogui.press('enter')
    time.sleep(4)

    #Fecha o programa

    pyautogui.hotkey('alt','f4')

pesquisa_navegador()