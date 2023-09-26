#Venta juguetería
PESO_PAYASO = 112
PESO_MUNECA = 75
venta_payasos = int(input("¿Cuantos payasos se han vendido?: "))
venta_muñecas = int(input("¿Cuantas muñecas se han vendido?: "))
peso_total = PESO_PAYASO*venta_payasos+venta_muñecas*PESO_PAYASO

print("El peso total del paquete es",peso_total,"gramos")