# programa para adivinar el numero
import random

# 1. El ordenador elige un número y preparamos el contador
numero_secreto = random.randint(1, 100)
intento = None
contador_intentos = 0

print("--- ¡Juego de Adivinanza! ---")
print("He pensado un número entre 1 y 100.")

# 2. El bucle se repite hasta que el usuario acierte
while intento != numero_secreto:
    try:
        intento = int(input("¿Cuál es tu suposición?: "))
        contador_intentos += 1 # Incrementamos el contador en cada turno
        
        # 3. Damos pistas
        if intento < numero_secreto:
            print("Más alto ↑")
        elif intento > numero_secreto:
            print("Más bajo ↓")
        else:
            # 4. Mensaje de victoria con el total de intentos
            print(f"¡Felicidades! Lo lograste en {contador_intentos} intentos.")
            
    except ValueError:
        print("Error: Por favor, introduce un número entero.")

print("Fin del juego.")
