# Modulo para ordenar pizzas y emitir la facturas.

# Datos base de refencia
producto = "Pizzas 🍕"
precio = int(10)
iva = float(1.19)
tipoMoneda = ['USD', 'EUR', 'COP']

# Tomar la orden al cliente
name = input("¿Nombre para el pedido?: ")
addres = input("¿Dirección de entrega?: ")
cuantasPizzas = int(input("¿Cuantas pizzas desea ordenar? 🍕: "))
totalConIva = precio * iva
totalOrden = round((totalConIva * cuantasPizzas),3)
print (f"{name}, Su pedido es de: ${totalOrden} {tipoMoneda[0]}")
ordenar = input("¿Desea continuar con la orden?. ¿Si o No? 👉:")
if ordenar.lower() == "si":
    print("Su orden ha sido procesada")
elif ordenar.lower() == "no":
    print("Si orden ha sido cancelada y no se ha generado ningun cobro")
else:
    print("Su orden ha sido cancelada porque no marco un valor valido")
ticket = f"Invoice #PH-789 PizzasPyThon🍕 • El precio total de su orden, que incluye {cuantasPizzas} {producto} es de $ {totalOrden}  {tipoMoneda[0]}"
# print(ticket)

# El tickete solo se imprime si la orden es mayor 20 y 30 Dolares
if totalOrden >= 20 and ordenar == "Si":
    print(ticket)