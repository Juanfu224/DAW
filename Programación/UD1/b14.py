"""Escribe un programa que pida al usuario que ingrese 3 valores que representan el número total de alumnos, el número de chicas y el número de chicos y luego los muestre por pantalla:
El número total de alumnos es: 
El número de chicas es:
El número de chicos es:"""

# Dividir la entrada en una lista de valores
entrada = input("Ingrese el número total de alumnos, número de chicas y número de chicos (separados por espacios): ")

# Dividir la entrada en una lista de valores
valores = entrada.split()

# Asignar los valores a variables
total_alumnos = int(valores[0])
chicas = int(valores[1])
chicos = int(valores[2])

print("El número total de alumnos es:", total_alumnos)
print("El número de chicas es:", chicas)
print("El número de chicos es:", chicos)