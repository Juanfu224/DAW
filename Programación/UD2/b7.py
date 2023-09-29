"""Solicite una letra al usuario. Si la letra leída es ‘L’, ‘M’, ‘X’, ‘J’ o ‘V’ se mostrará por pantalla: 
“El día elegido es entre semana”. Si la letra es ‘S’ o ‘D’ se mostrará el siguiente mensaje: 
“El día elegido es fin de semana”. En cualquier otro caso se mostrará un error."""

letra = input("Dime una letra (‘L’,‘M’,‘X’,‘J’‘V’,‘S’o‘D’): ")

match letra:
    case "L"|"M"|"X"|"J"|"V":
        print("El día elegido es entre semana")
    case "S"|"D":
        print("El día elegido es fin de semana")
    case _:
        print("ERROR")