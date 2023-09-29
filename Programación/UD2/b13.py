"""Lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400."""

year = int(input("Dime el año que quieres saber si es bisiesto: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("El año", year, "es bisiesto")
else:
    print("El año", year, "no es bisiesto")