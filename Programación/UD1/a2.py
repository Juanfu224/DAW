#Horas trabajados y cuanto gano
horas = int(input("¿Cuantas horas trabajas al mes?: "))
dinero = float(input("¿Cuanto dinero ganas cada hora?: "))

#Calculo
total = horas * dinero
print("Ganas",str(total)+"€ al mes")