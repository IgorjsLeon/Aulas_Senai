import pyautogui
import time

#Função para desenhar uma estrela

def desenhar_estrela(x, y, tamanho):
    pyautogui.click(x, y) #Clica no ponto inicial no Paint

    #Calcular os pontos da estrela
    pontas = 5
    angulo = 360 / pontas
    raio_externo = tamanho
    raio_interno = tamanho/2

    for i in range(pontas*2):
        if i % 2 != 0:
            pyautogui.dragTo(raio_interno, 0, duration=1)
            #Desenha a linha interna
        else:
            pyautogui.dragRel(raio_externo, 0, duration=1)
            #Desenha linha externa
    
    pyautogui.moveRel(0, 0)

    #Aguardar alguns segundos
    time.sleep(2)

    #Coordenadas do ponto inicial e tamanho da estrela
    x_inicial, y_inicial = 100, 100
    tamanho_estrela = 50
