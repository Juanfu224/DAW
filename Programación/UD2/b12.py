""" Lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar qué tipo de triangulo es,
teniendo en cuenta los siguiente:
    • Si se cumple Pitágoras entonces es triángulo rectángulo
    • Si sólo dos lados del triángulo son iguales entonces es isósceles.
    • Si los 3 lados son iguales entonces es equilátero.
    • Si no se cumple ninguna de las condiciones anteriores, es escaleno."""

lado_A = float(input("Dime cuanto mide el lado A: "))
lado_B = float(input("Dime cuanto mide el lado B: "))
lado_C = float(input("Dime cuanto mide el lado C: "))

rectangulo = lado_A**2 == lado_A**2 +lado_B**2 
equilatero = lado_A == lado_B == lado_C
isosceles = lado_A == lado_B !=lado_C or lado_A != lado_B ==lado_C or lado_A == lado_C !=lado_B

if rectangulo:
    print("Es rectángulo")
elif equilatero:
    print("Es rectángulo")
elif isosceles:
    print("Es isósceles")
else:
    print("Es escaleno")