#Venta juguetería
peso_payaso = 112
peso_muñeca = 75
venta_payasos = int(input("¿Cuantos payasos se han vendido?: "))
venta_muñecas = int(input("¿Cuantas muñecas se han vendido?: "))
peso_total = peso_payaso*venta_payasos+venta_muñecas*peso_muñeca

print("El peso total del paquete es",peso_total,"gramos")