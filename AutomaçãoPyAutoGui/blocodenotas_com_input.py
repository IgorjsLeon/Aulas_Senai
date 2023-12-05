import pyautogui
import time

def bloco_de_notas_com_input():
    #Pede os inputs do usuario para a mensagem a ser escrita e o nome do arquivo a ser salvo.
    texto= input("Digite um texto para o arquivo: ")
    nome_Salvar= input("Digite um nome para o arquivo: ")
    time.sleep(1)

    #Abre o programa

    pyautogui.press('winleft')
    programa = 'Bloco de notas'
    pyautogui.write(programa)
    pyautogui.press('enter')
    time.sleep(2)

    #Escreve a mensagem do usuario

    pyautogui.write(texto)
    time.sleep(1)

    #Abre o terminal de salvar

    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)

    #Digita o nome do arquivo que o usuario deseja

    pyautogui.write(f'{nome_Salvar}.txt')
    time.sleep(1)

    #Confirmar a ação

    pyautogui.press('enter')
    time.sleep(1)

    #Finaliza fechand o programa

    pyautogui.hotkey('alt', 'f4')

bloco_de_notas_com_input()