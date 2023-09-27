"""Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “1234”
se indica “Has entrado al sistema”, sino se da un error."""

usuario = input("Dime el usuario: ")
contrasena = int(input("Dime la contraseña: "))

if usuario=="pepe" and contrasena==1234:
    print("Has entrado al sistema")
else:
    print("ERROR")