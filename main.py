import msvcrt
import os
import pygame

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
while (jugando):
    for palabra in palabras :        
        for letra in palabra :
            if (puntuacion < 10) :
                string_puntuacion = "-" + str(puntuacion)
            else :
                string_puntuacion = str(puntuacion)
            if (vidas > 0) :
                print(tablero.format(string_puntuacion,str(vidas),letra))
                tecla_presionada = msvcrt.getwch()
                sonido.play()
                print(tecla_presionada)
                if (tecla_presionada == " ") :
                    jugando = False
                    break
                elif (tecla_presionada == letra) :
                    puntuacion = puntuacion + 1
                else :
                    vidas = vidas - 1
            else :
                print("You loose")
                print("Score:{}".format(str(vidas)))
                jugando = False
                break
    if (jugando == True) :
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