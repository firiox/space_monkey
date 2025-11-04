import msvcrt

palabras = ["silla","dedo","teclado","bueno","killua","zanahoria"]
jugando = True
tablero = "------{}\n--------\n------{}-\n--------\n{}-------\n--------"
puntuacion = 0
string_puntuacion = ""
vidas = 3
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