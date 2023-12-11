import pyautogui
import time

#Aguarda 5 segundos 
time.sleep(2)

#Obtenha e imprima as dimensões da tela

largura, altura = pyautogui.size()
print(f"A largura da tela é {largura} e a altura da tela {altura}")

# Mover o mouse para as coordenadas (x, y) e clicar em algo

pyautogui.moveTo(100, 100, duration=1.5)
pyautogui.click()

#Digite usando um teclado virtual

pyautogui.typewrite("Hello, World!")

#Captura de tela

captura_Tela = pyautogui.screenshot()
captura_Tela.save("Minha_Tela.png")

#Exemplo de múltiplos cliques e intervalos entre cliques

pyautogui.click(200,200, clicks=2, interval=0.5, button='left')

#Exemplo pressionar uma tecla

pyautogui.press('enter')

#Rolar tela para cima

pyautogui.scroll(100)

#Exibir um alerta

pyautogui.alert("Seu computador foi infectado!")

#obtem e imprime a posição atual do cursos do mouse

x ,y= pyautogui.position()
print(f"A posição atual do mouse é x = {x}, y= {y}")

#Obtém e imprime a posição do mouse continuamente
while True:
    x, y = pyautogui.position()
    print( f"posição x = {x} e y = {y}")

    pyautogui.dragTo(600,600, duration=1, button='left')






