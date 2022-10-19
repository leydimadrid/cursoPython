# Una lista en Python es un tipo de contenedor que permite almacenar datos.
# [ Alt + 91
# ] Alt + 93

listaCompras = ['Computador', 50, 'Mouse', 'Teclado']
# Para seleccionar un solo artículo de la variable anterior
articuloSeleccionado = listaCompras[2]
listaCompras.append(58)  # Agregar un elemento a la lista
listaCompras[0] = "NuevoComputador"  # Reemplazar algún elemento existente

print(listaCompras)
print("La lista compras tiene", len(listaCompras),"elementos")  # Cual es la longitud de la variable
print(listaCompras[-2])  # Cuál es el último elemento de la lista
# Este método nos permite saber cuántos elementos iguales hay en la lista
# Sirve para saber cuántos elementos del mismo tipo existen
print(listaCompras.count("Teclado"))
# Este método nos busca cuál es la primera posición del elemento solicitado
print(listaCompras.index("Teclado"))
# Inserta un nuevo elemento en la posición que le indiquemos
listaCompras.insert(2, "ElementoNuevo")
print(listaCompras)
listaCompras.pop()  # Devuelve el último elemento de la lista y lo borra, si queremos especificar una posición debemos colocarla dentro del ()
print(listaCompras)
print(listaCompras[0:2]) #Acá obtenemos los elementos que hay entre dichas posiciones

