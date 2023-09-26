#Escribe un programa que permita convertir temperaturas dadas en grados Celsius a temperaturas en grados Farenheit y viceversa

celsius = int(input("Dime los grados Celsius que deseas convertir a Farenheit: "))
calculo_farenheit = celsius*9/5
salida = print(celsius,"ºCelsius son",round(calculo_farenheit,2),"ºFarenheit")

farenheit = int(input("Dime los grados Farenheit que deseas convertir a Celsius: "))
calculo_celsius = (farenheit-32)*5/9
salida = print(farenheit,"ºFarenheit son",round(calculo_celsius),"ºCelsius")