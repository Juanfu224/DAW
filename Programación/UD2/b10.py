"""Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, 
la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’.
Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’."""

notas = int(input("¿Cuál es tu nota?: "))
edad = int(input("¿Cuál es tu edad?: "))
sexo = input("¿Cuál es tu sexo? (F,M): ")

if notas >= 5:
    if edad >= 18:
        if sexo == "F":
            print("ACEPTADA")
        elif sexo == "M":
            print("POSIBLE")
        else:
            print("El sexo debe ser 'F' o 'M'.")
    else:
        print("La edad debe ser mayor o igual a 18.")
else:
    print("NO ACEPTADA")