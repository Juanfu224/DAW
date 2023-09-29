"""    12. Escribe un programa que pida al usuario dos números y los intercambie. Es decir, que, tras guardarlos, en donde guardaba el primero guarde el segundo y viceversa. 
Ejemplo: 
 	n1=2        n2=3
Intercambiamos los valores 
Mostrar n1 (debe contener el valor 3) 
Mostrar n2 (debe contener el valor 2) """

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

n1, n2 = n2, n1

print("Intercambiamos los valores")
print("n1 contiene el valor:", n1)
print("n2 contiene el valor:", n2)