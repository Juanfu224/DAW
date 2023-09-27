"""Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario."""
numero1 = int(input("Dime el primer número: "))
numero2 = int(input("Dime el segundo número: "))

if numero2 == 0:
    print("Error, no se puede dividir entre 0")
else:
    print(numero1/numero2)