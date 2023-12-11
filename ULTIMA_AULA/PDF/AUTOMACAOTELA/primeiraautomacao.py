import pyautogui
import time

#Função para o Bloco de Notas e Digitar uma Mensagem

def escrever_no_bloco():
    #Abre o bloco de notas
    pyautogui.press('winleft')
    procura = "bloco"
    pyautogui.write(procura)
    time.sleep(1)
    pyautogui.press('enter')


    #Aguarda a abertura do bloco de notas
    time.sleep(3)


    #Digita uma mensagem

    mensagem = "Vixi, virus!"
    pyautogui.write(mensagem)

#Função para salvar o arquivo no Bloco de Notas

def salvar_no_bloco():
    #Atalho para salvar ( Ctrl + S)
    pyautogui.hotkey('ctrl', 's')

    #Aguarda a janela de salvamento abri
    time.sleep(2)

    #Dogita o nome do arquivo
    nome_arquivo = "virus.txt"
    pyautogui.write(nome_arquivo)

    #Pressiona Enter para salvar
    pyautogui.press('enter')

#Chama as funções

escrever_no_bloco()
time.sleep(1.5)
salvar_no_bloco()