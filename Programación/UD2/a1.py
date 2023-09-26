"""Escribe un programa que pida al usuario dos números y muestre su división. Si el divisor es
cero la división no se hace y se muestra el mensaje de “error no se puede dividir por cero”"""

x = int(input("Dime el dividendo: "))
y = int(input("Dime el divisor: "))

if y == 0:
    print("Error, no se puede dividir por cero")
else:
    print(x/y)