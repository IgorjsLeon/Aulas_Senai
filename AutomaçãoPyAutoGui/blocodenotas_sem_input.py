'''Criar uma automação com pyautogui pela qual o programa abre o bloco de notas, digita uma mensagem e a salva'''
import pyautogui
import time

def bloco_de_notas():
    #Abrir o bloco de notas
    time.sleep(1)
    pyautogui.press('winleft')
    programa = 'Bloco de notas'
    pyautogui.write(programa)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('Hello, World!')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.write('Automatizacao Bloco de Notas.txt')
    time.sleep(1)
    pyautogui.press('enter')
bloco_de_notas()

