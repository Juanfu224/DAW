"""Solicite 5 números calcule la media aritmética la muestre y también muestre los que sean mayores que la media."""
numero1 = int(input("Dime el 1º número: "))
numero2 = int(input("Dime el 2º número: "))
numero3 = int(input("Dime el 3º número: "))
numero4 = int(input("Dime el 4º número: "))
numero5 = int(input("Dime el 5º número: "))

media = (numero1+numero2+numero3+numero4+numero5)/5
print ("La media aritmética es:",media)

if numero1 > media:
    print("El número",numero1,"es mayor que la media.")
if numero2 > media:
    print("El número",numero2,"es mayor que la media.")
if numero3 > media:
    print("El número",numero3,"es mayor que la media.")
if numero4 > media:
    print("El número",numero4,"es mayor que la media.")
if numero5 > media:
    print("El número",numero5,"es mayor que la media.")