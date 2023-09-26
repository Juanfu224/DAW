"""Escribe un programa que pida la edad al usuario y si es menor que 18 muestre por pantalla
“Es usted menor de edad” si no que muestre “Es usted mayor de edad” y al finalizar que
muestre “¡Hasta la próxima!”"""

pregunta = input("¿Cuantos años tienes?")

if pregunta >= 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")

print("¡Hasta la próxima!")