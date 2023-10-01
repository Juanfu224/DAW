"""Muestre la tabla de multiplicar de un número introducido por teclado."""
numero = int(input("Dime un número: "))
cont = 0
while cont <= 10:
    calculo = numero*cont
    print(calculo)
    cont+=1