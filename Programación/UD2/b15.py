"""La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2.
Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque,
considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2.
Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida."""


precio_kilo_uva = float(input("¿A cuanto está el kilo de uva?: "))
tipo_uva = input("¿Tipo de uva (A/B)?: ")
tamanio_uva = int(input("¿Tamaño de uva (1/2)?: "))

precio_A1 = precio_kilo_uva+0.20
precio_A2 = precio_kilo_uva+0.30
precio_B1 = precio_kilo_uva-0.30
precio_B2 = precio_kilo_uva-0.50

if tipo_uva == 'A':
    if tamanio_uva == 1:
        precio_final = precio_A1
    elif tamanio_uva == 2:
        precio_final = precio_A2
    else:
        print("Tamaño de uva no válido")
elif tipo_uva == 'B':
    if tamanio_uva == 1:
        precio_final = precio_B1
    elif tamanio_uva == 2:
        precio_final = precio_B2
    else:
        print("Tamaño de uva no válido")
else:
    print("Tipo de uva no válido")

print("El precio final por kilo de uva es:",precio_final,"euros.")