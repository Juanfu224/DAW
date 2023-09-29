"""Pida tres números y los muestre ordenados (de mayor a menor);"""
numero1 = int(input("Dime el 1º número: "))
numero2 = int(input("Dime el 2º número: "))
numero3 = int(input("Dime el 3º número: "))

if numero1 > numero2 > numero3:
    print("El orden de mayor a menor es:",numero1,numero2,numero3)
elif numero1 > numero3 > numero2:
    print("El orden de mayor a menor es:",numero1,numero3,numero2)
elif numero2 > numero1 > numero3:
    print("El orden de mayor a menor es:",numero2,numero1,numero3)
elif numero2 > numero3 > numero1:
    print("El orden de mayor a menor es:",numero2,numero3,numero1)
elif numero3 > numero1 > numero2:
    print("El orden de mayor a menor es:",numero3,numero1,numero2)
elif numero3 > numero2 > numero1:
    print("El orden de mayor a menor es:",numero3,numero2,numero1)
else:
    print("Todos los números son iguales")