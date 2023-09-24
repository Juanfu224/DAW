# Suma de todos los enteros desde 1 hasta n.
x = int(input("Dime un número entero positivo: "))
y = 1
while x != y:
    print(x*(x+y)/2)
    y+=1