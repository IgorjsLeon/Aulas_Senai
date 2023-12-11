import pyautogui
import time

# Função para realizar a automação no Bloco de Notas
def automacao_bloco_notas():
    # Abrir o primeiro Bloco de Notas
    pyautogui.hotkey('winleft')  # Pressionar a tecla Windows para abrir o menu Iniciar
    pyautogui.write('bloco de notas')  # Escrever "bloco de notas" para pesquisar
    time.sleep(1)  # Aguardar um segundo para o resultado da pesquisa
    pyautogui.press('enter')  # Pressionar Enter para abrir o Bloco de Notas
    time.sleep(2)  # Aguardar alguns segundos para o Bloco de Notas abrir completamente

    # Digitar um texto no primeiro Bloco de Notas
    texto_original = "Este é um texto de exemplo."
    pyautogui.write(texto_original)

    # Selecionar todo o texto
    pyautogui.hotkey('ctrl', 'a')

    # Copiar o texto
    pyautogui.hotkey('ctrl', 'c')

    # Abrir o segundo Bloco de Notas
    pyautogui.hotkey('winleft')  # Pressionar a tecla Windows para abrir o menu Iniciar
    pyautogui.write('bloco de notas')  # Escrever "bloco de notas" para pesquisar
    time.sleep(1)  # Aguardar um segundo para o resultado da pesquisa
    pyautogui.press('enter')  # Pressionar Enter para abrir o segundo Bloco de Notas
    time.sleep(2)  # Aguardar alguns segundos para o Bloco de Notas abrir completamente

    # Colar o texto no segundo Bloco de Notas
    pyautogui.hotkey('ctrl', 'v')

# Esperar alguns segundos antes de começar
time.sleep(5)

# Chamar a função de automação
automacao_bloco_notas()
