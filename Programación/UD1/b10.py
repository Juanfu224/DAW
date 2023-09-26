#Escribe un programa que pida un número decimal, y muestra por separado su parte entera y su parte decimal.
numero = float(input("Dime un número decimal: "))
parte_entera = int(numero)
decimal = numero-parte_entera

print("Su parte entera es",int(parte_entera),"y su parte decimal es",round(decimal,2))