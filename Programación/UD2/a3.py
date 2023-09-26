"""Escribe un programa que haga de calculadora: le pide dos números al usuario y la operación
a realizar. Finalmente muestra en pantalla el resultado de la operación."""

x = input("Dime el 1º número: ")
y = input("Dime el 2º número: ")
op = input("Ingresa la operación (+,-,/,*): ")

if op == "+":
    print(x+y)
elif op == "-":
     print(x-y)
elif op == "/":
    if y == 0:
        print("Error, no se puede dividir por cero")
    else:
        print(x/y)
elif op == "*":
     print(x*y)
else:
    print("Operación desconocida")