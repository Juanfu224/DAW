"""Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “1234”
se indica “Has entrado al sistema”, sino se da un error."""
NOMBRE = "pepe"
CONTRASENA = 1234
usuario = input("Dime el usuario: ")
contrasena = int(input("Dime la contraseña: "))

if usuario==NOMBRE and contrasena==CONTRASENA:
    print("Has entrado al sistema")
else:
    print("ERROR")