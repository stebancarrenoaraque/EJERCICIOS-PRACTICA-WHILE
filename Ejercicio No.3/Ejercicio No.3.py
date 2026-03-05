# programa para adivinar el numero
import random

numero = random.randint(1,100)
intento = 0
while intento != numero:
    intento = int(input("adivina el numero desde el 1 al 100: "))

    if intento < numero:
        print("el numero es mas alto")
    elif intento > numero:
        print(" el numero es mas bajo")

print("FELICIDADES HAS ADIVINADO EL NUMERO :) ")