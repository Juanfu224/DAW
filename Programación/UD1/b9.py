#Escribe un programa que lea 4 datos enteros, calcule su producto, su suma y su media aritmética.
numero1 = int(input("Dime el primer número: "))
numero2 = int(input("Dime el segundo número: "))
numero3 = int(input("Dime el tercer número: "))
numero4 = int(input("Dime el cuarto número: "))
producto = numero1*numero2*numero3*numero4
suma = numero1+numero2+numero3+numero4
media = suma/4

print("El producto entre los 4 números es",producto)
print("La suma entre los 4 números es",suma)
print("La media entre los 4 números es",media)