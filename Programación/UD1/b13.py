"""Se tienen tres variables A, B y C de tipo carácter. Escribe un programa que haga los siguientes intercambios usando sólo una variable auxiliar: 
B toma el valor de A. 
C toma el valor de B. 
A toma el valor de C. """

a = input("Ingrese el valor para A: ")
b = input("Ingrese el valor para B: ")
c = input("Ingrese el valor para C: ")

temp = a
a = b
b = c
c = temp

print("Después de los intercambios:")
print("A contiene el valor:", a)
print("B contiene el valor:", b)
print("C contiene el valor:", c)

#a,b,c=b,c,a



