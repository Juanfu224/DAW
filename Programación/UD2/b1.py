"""Programa que pida dos números e indique si el primero es mayor que el segundo o no."""
numero1 = int(input("Dime el primer número: "))
numero2 = int(input("Dime el segundo número: "))

if numero1 < numero2:
    print("El primero es menor que el segundo")
elif numero1 == numero2:
    print("Los dos números son iguales")
else:
    print("El primero es mayor que el segundo")