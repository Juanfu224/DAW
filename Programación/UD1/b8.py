#Descuento panadería
precio_pan = 3.49
descuento_pan = precio_pan * 0.40
ventas = int(input("¿Cuantas barras de pan se han vendido hoy que no son del dia?: "))
ventas_sin_descuento = precio_pan * ventas
ventas_descuento = descuento_pan * ventas

print("Normalmente el pan cuesta",str(precio_pan)+"€ cada uno, pero con el descuento son",str(descuento_pan)+"€. La venta total sin descuento es",
      str(ventas_sin_descuento)+"€ y con descuento es",str(ventas_descuento)+"€.")