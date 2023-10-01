"""Pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0."""
cont = int(input("¿Cuantos números quieres introducir?: "))
menores = 0
iguales = 0
mayores = 0
print("Tienes que poner en total", cont, "números.")

while cont != 0:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        menores += 1
    elif numero == 0:
        iguales += 1
    else:
        mayores += 1
    cont -= 1
print("\nHas dicho:\n",
      menores, "números menores que 0.\n",
      iguales, "números iguales que 0.\n",
      mayores, "números mayores que 0.")
