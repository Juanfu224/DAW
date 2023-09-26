#Descuento panadería
PRECIO_PAN = 3.49
descuento_pan = PRECIO_PAN * 0.40
ventas = int(input("¿Cuantas barras de pan se han vendido hoy que no son del dia?: "))
ventas_sin_descuento = PRECIO_PAN * ventas
ventas_descuento = descuento_pan * ventas

print("Normalmente el pan cuesta",PRECIO_PAN,"€ cada uno, pero con el descuento son",round(descuento_pan,2),"€.La venta total sin descuento es",
      round(ventas_sin_descuento,2),"€ y con descuento es",round(ventas_descuento,2),"€.")