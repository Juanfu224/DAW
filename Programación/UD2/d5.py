"""Imprima todos los números pares entre dos números que se le pidan al usuario."""
numero_1 = int(input("Dime el 1º número: "))
numero_2 = int(input("Dime el 2º número: "))

if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1
if numero_1 % 2 != 0:
    numero_1 += 1

for pares in range(numero_1,numero_2+1,2):
    if pares < numero_2-1: 
        print(pares, end=",")
    else:
        print(pares, end=".")