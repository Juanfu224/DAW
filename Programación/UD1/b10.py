#Escribe un programa que pida un número decimal, y muestra por separado su parte entera y su parte decimal.
import math
numero = float(input("Dime un número decimal: "))
parte_decimal, parte_entera = math.modf(numero)
print("Su parte entera es {} y su parte decimal es {}".format(int(parte_entera),round(parte_decimal,2)))