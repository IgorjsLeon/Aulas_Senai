import pyautogui
import time

#Aguardar alguns segundos antes de iniciar
time.sleep(5)

#Obtenha e imprima as dimensões da tela
"""largura, altura = pyautogui.size()
print(f"A lagura da tela é: {largura}\n. A altura da tela: {altura}.")

#Mover o mouse para as coordenadas (x,y) e clique

pyautogui.move(200, 200, duration=1)
pyautogui.click()

#Digite algo usando o teclado virtual
pyautogui.typewrite("Hello, world!")"""

#Obter e imprimir a posição atual do mouse

while True:
    x,y = pyautogui.position()
    print(f"A posição atual do mouse é {x} and {y}.")

#Exibir um alerta

pyautogui.alert("Este é um alerta!")