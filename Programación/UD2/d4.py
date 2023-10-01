"""Pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio."""
while True:
    caracter = input("Introduce un carácter: ")
    match caracter:
        case "a" | "e" | "i" | "o" | "u":
            print("VOCAL")
        case " ":
            break
        case _:
            print("NO VOCAL")
