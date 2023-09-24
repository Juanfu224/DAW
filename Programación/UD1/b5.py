#Calcular masa corporal
peso = int(input("¿Cuanto kilogramos pesas?:\n"))
altura = float(input("¿Cuantos metros mides?\n"))
total = float(peso / altura**2)
imc = float(round(total,2))

print("Tu índice de masa corporal es",imc)