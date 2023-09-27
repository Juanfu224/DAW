"""Solicite un número e indique si es múltiplo de 2, de 5, de ambos o de ninguno."""
numero = int(input("Dime un número: "))

if numero%2==0 and numero%5==0:
    print("El número es multiplo de 2 y de 5")
elif numero%2==0:
    print("El número es multiplo de 2")
elif numero%5==0:
    print("El número es multiplo de 5")
else:
    print("El número no es multiplo de ninguno")