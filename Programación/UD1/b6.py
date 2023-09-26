#divisiones
numero_1 = int(input("¿Dime el 1º número?: "))
numero_2 = int(input("¿Dime el 2º número?: "))
total = int(numero_1 / numero_2)
resto = int(numero_1 % numero_2)

print(numero_1,"entre",numero_2,"da un cociente",
      total,"y un resto",resto)