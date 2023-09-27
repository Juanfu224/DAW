"""Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
    • El exponente sea positivo, sólo tienes que imprimir la potencia.
    • El exponente sea 0, el resultado es 1.
    • El exponente sea negativo, el resultado es 1/potencia con el exponente positivo."""

base = int(input("Dime el número base: "))
exponente = int(input("Dime el exponente: "))
calculo = base**exponente

if exponente > 0:
    print(calculo)
elif exponente == 0:
    print("1")
else:
    exponente = abs(exponente)
    calculo = 1/base**exponente
    print(calculo)