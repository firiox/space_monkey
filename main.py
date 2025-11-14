import msvcrt
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import time
from utilities import clear

palabras = ["silla","dedo","teclado","bueno","killua","zanahoria"]
jugando = True
tablero = "------{}\n--------\n------{}-\n--------\n{}-------\n--------"
puntuacion = 0
string_puntuacion = ""
vidas = 3
tecla_presionada = ""
# Evitar que se abra una ventana
os.environ["SDL_VIDEODRIVER"] = "dummy"
# Inicializar solo el mezclador de sonido
pygame.mixer.init()
# Cargar el sonido
sonido = pygame.mixer.Sound("sonido-boton.wav")
error = pygame.mixer.Sound("error-beep.wav")
# Antes del bucle principal
point_sound = pygame.mixer.Channel(0)
error_sound = pygame.mixer.Channel(1)
clear()
print("3")
time.sleep(1)
clear()
print("2")
time.sleep(1)
clear()
print("1")
time.sleep(1)
clear()
while (jugando):
    for palabra in palabras :
        if (jugando == False) :
            break
        else :
            for letra in palabra :
                if (puntuacion < 10) :
                    string_puntuacion = "-" + str(puntuacion)
                else :
                    string_puntuacion = str(puntuacion)
                if (vidas > 0) :
                    clear()
                    print(tablero.format(string_puntuacion,str(vidas),letra))
                    tecla_presionada = msvcrt.getwch()
                    
                    print(tecla_presionada)
                    if (tecla_presionada == " ") :
                        jugando = False
                        break
                    elif (tecla_presionada == letra) :
                        puntuacion = puntuacion + 1
                        #Reproduce el sonido cuando acierta la tecla
                        point_sound.play(sonido)                        
                    else :
                        vidas = vidas - 1
                        #Reproduce el sonido cuando falla la tecla
                        error_sound.play(error)
                else :
                    #Esperamos a que el sonido termine
                    while error_sound.get_busy():
                        time.sleep(0.05)
                    print("You loose")
                    print("Score:{}".format(str(puntuacion)))
                    jugando = False
                    break
    if (jugando == True) :
        #Esperamos a que el sonido termine
        while point_sound.get_busy():
            time.sleep(0.05)
        print("You win")
        print("Score:{}".format(str(puntuacion)))
        jugando = False
    else :
        pass



"""
"------Y-"
"--------"
"------Z-"
"--------"
"X-------"
"--------"
"""

