"""Escribe un programa que pida al usuario un número entero positivo y muestre por pantalla
todos los números impares desde 1 hasta ese número separados por comas"""

numero = int(input("Dime un número entero: "))
for impares in range(1, numero, 2):
    if impares < numero-1:
        print(impares, end=",")
    else:
        print(impares, end=".")
