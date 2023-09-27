"""Solicite una letra al usuario. Si la letra leída es ‘L’, ‘M’, ‘X’, ‘J’ o ‘V’ se mostrará por pantalla: 
“El día elegido es entre semana”. Si la letra es ‘S’ o ‘D’ se mostrará el siguiente mensaje: 
“El día elegido es fin de semana”. En cualquier otro caso se mostrará un error."""

letra = input("Dime una letra (‘L’,‘M’,‘X’,‘J’‘V’,‘S’o‘D’): ")

match letra:
    case "L":
        print("El día elegido es entre semana")
    case "M":
        print("El día elegido es entre semana")
    case "X":
        print("El día elegido es entre semana")
    case "J":
        print("El día elegido es entre semana")
    case "V":
        print("El día elegido es entre semana")
    case "S":
        print("El día elegido es fin de semana")
    case "D":
        print("El día elegido es fin de semana")
    case _:
        print("ERROR")