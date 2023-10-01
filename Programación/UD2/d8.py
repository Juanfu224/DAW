"""Que saque por pantalla el resultado de la potencia, dados dos números, uno real (base) y un entero positivo (exponente),
No se puede utilizar el operador de potencia."""
import math

base = int(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))
potencia = math.pow(base,exponente)

print(int(potencia))