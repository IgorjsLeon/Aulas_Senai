'''Criar um script que digite um texto no bloco de notas, copie e cole o mesmo texto em outro bloco de notas'''
import pyautogui
import time

def exercicio():
    texto = input("Digite um texto: ")
    time.sleep(1)

    pyautogui.press('winleft')
    pyautogui.write('Bloco de notas')
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.write(texto)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    pyautogui.press('winleft')
    pyautogui.write('Bloco de notas')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'v')

exercicio()