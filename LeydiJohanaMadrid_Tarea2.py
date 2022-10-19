#Realice un código que capture por medio de consola 3 nombres de productos y 3 precios.

productoUno = str(input("Ingrese el primer producto: ").upper())
precioUno = int(input("Precio del producto: "))
productoDos = str(input("Ingrese el segundo producto: ").upper())
precioDos = int(input("Precio del producto: "))
productoTres = str(input("Ingrese el tercer producto: ").upper())
precioTres = int(input("Precio del producto: "))

#Suma de los 3 productos
sumaProductos = precioUno + precioDos + precioTres

#Iva del 19%
Iva = float(0.19)
ivaProductos = sumaProductos * Iva
totalConIva = sumaProductos + ivaProductos


#Muestre cada producto y precio
print("\n---FACTURA DE VENTA---\n")
print(f"1-  {productoUno}: {precioUno}")
print(f"2-  {productoDos}: {precioDos}")
print(f"3-  {productoTres}: {precioTres}")

#Muestre el valor de la sumatoria de todos los precios de los productos.
print(f"\nEl valor total de los productos es de: {sumaProductos}\n")

#Muestre el precio del IVA que es del 19% del total.
print(f"Iva: {ivaProductos}")

#Muestre el valor total sumando el IVA.
print(f"El valor total con Iva incluido es: {totalConIva}" )


