# Juego de python en el que el jefe te va quitando vida hasta que se acaba

import random

vida = 50

while vida > 0:
    daño = random.randint(5,15)
    vida = vida - daño

    print("el jefe te quito:", daño, "de vida")
    print("vida restante:",vida)
    if vida < 0:
        print("tu vida llego a 0. perdiste la pelea")
        break