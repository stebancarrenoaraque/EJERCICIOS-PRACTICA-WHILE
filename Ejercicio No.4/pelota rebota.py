# Ejercicio 4
h = int(input("altura inicial h(metros): "))
if h <= 0:
    print("La altura debe ser positiva.")
else:
    limite = h / 5.0
    rebote = 1
    altura_rebote = h * 0.9
while altura_rebote  >= limite:
    rebote += 1 
    altura_rebote *= 0.9

    print("la altura No alcanza a subir la quinta parte de la altura inicial en el rebote numero" + str(rebote))
    print("Altura en ese rebote" + str(altura_rebote))