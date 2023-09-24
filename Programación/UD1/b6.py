#divisiones
numero_1 = int(input("¿Dime el 1º número?: "))
numero_2 = int(input("¿Dime el 2º número?: "))
total = int(numero_1 / numero_2)
resto = int(numero_1 % numero_2)

print(str(numero_1),"entre",str(numero_2),"da un cociente",
      str(total),"y un resto", str(resto))