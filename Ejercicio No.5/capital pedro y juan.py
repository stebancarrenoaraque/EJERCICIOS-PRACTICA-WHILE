c1 = int(input("capital de pedro: "))
c2 = int(input("capital de juan: "))
c3 = int(input("capital nesesario para el negocio: "))

mes = 0
cap1 = c1
cap2 = c2

while cap1 + cap2 > c3:
    mes = mes + 1
    cap1 = cap1 * 1.03
    cap2 = cap2 * 1.04

print("pueden hacer el negocio en" , mes)
print("capital total" , cap1 + cap2)