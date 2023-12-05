#pip install pyautogui para instalar a biblioteca

import pyautogui
import time

#Aguardar alguns seguindos antes de iniciar

time.sleep(2)

#Obtenha e imprima as dimensões da tela

largura, altura = pyautogui.size()
print(f"A largura da tela é {largura} e a altura é {altura}\n")

#Mover o mouse para as coordenadas (x,y) e clicar

pyautogui.move(200, 200, duration=1)
pyautogui.click()

#Digite algo usando o teclado virtual

pyautogui.typewrite("Hello, world!")

#Obter e imprimir a posição atual do mouse

x,y = pyautogui.position()
print(f'A posição atual do mouse é x: {x} e y: {y}')

#Exibir um alerta

pyautogui.alert("Este é um alerta")