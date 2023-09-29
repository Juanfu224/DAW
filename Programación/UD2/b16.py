"""El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía
de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos,
el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje."""
numero_alumnos = int(input("Ingrese el número de alumnos: "))

if numero_alumnos >= 100:
    costo_por_alumno = 65
elif 50 <= numero_alumnos < 100:
    costo_por_alumno = 70
elif 30 <= numero_alumnos < 50:
    costo_por_alumno = 95
else:
    costo_por_alumno = 0

costo_por_alumno, costo_autobus = calcular_costos(numero_alumnos)
total_a_pagar_compania = costo_por_alumno * numero_alumnos + costo_autobus

print("Cada alumno debe pagar",costo_por_alumno,"euros.")
print("El total a pagar a la compañía de autobuses es de",total_a_pagar_compania,"euros.")