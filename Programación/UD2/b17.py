"""La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura,
de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos,
y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana,
15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada."""

minutos_duracion = int(input("¿Cuanto ha durado la llamada?:"))
dia_semana = input("Introduce el dia de la semana en el que se realizó la llamada:")
turno = input("Introduce el turno en el que se realizó la llamada:")
coste_llamada = 0
impuesto = 0
costel_total = 0

if minutos_duracion <= 5:
        coste_llamada = minutos_duracion * 1.0
elif minutos_duracion <= 8:
    coste_llamada = 5 * 1.0 + (minutos_duracion - 5)* 0.8
elif minutos_duracion <= 10:
    coste_llamada = 5 * 1.0 + 3 * 0.8 + (minutos_duracion 8)* 0.7
else:
    coste_llamada = 5 * 1.0 + 3 * 0.8+ 2 * 0.7+ (minutos_duracion 10) * 0.5

if dia_semana == "domingo":
    impuesto = coste_llamada * 0.03
elif turno == "mañana":
    impuesto = coste_llamada * 0.15
elif turno == "tarde":
    impuesto coste_llamada 0.10

coste_total = coste_llamada + impuesto
print("El coste total de la llamada es de", round (coste_total, 2), "Euros.")
