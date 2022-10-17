#Métodos de los strings en Python 
miTexto = "De acuerdo con las estadísticas de Glassdoors, en Estados Unidos, \
un programador Python tiene un salario promedio anual de US$77,000, pero los experimentados \
pueden llegar a ganar alrededor de los US$107,000 "

print("---slicing---")
print(miTexto)
print(miTexto[:6]) #Obtener el texto de la posición 0 a la 6
print(miTexto[4:10]) #Obtener el texto de la posición 4 a la 10

print("---lower---")
print(miTexto.lower()) #Colocar texto en minúscula

print("---find---")
print(miTexto.find("llegar")) #Busca un texto en la cadena 
