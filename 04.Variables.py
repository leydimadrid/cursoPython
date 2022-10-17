"""
Definición variable:
'Una variable en programación es un elemento de datos cuyo valor puede cambiar.'
'Se identifica con un nombre único'

"""

nombre = "Brayan"
apellido = "Torres"
edad = 28 
valorpi = 3.1416
numero = "2703"
listas = ["vaso", "mesa", "radio"]


#El signo + es para sumar contenidos del mismo tipo o de string a número
print("Nombre y apellido:", nombre, apellido)
print("Edad: " + str(edad) ) #Convertir números a string
print("Número: ", int(numero)) #Convertir string a número
print(edad + int(numero))

print(type(valorpi)) #Con type podemos saber de que tipo es la variable
print(type(listas))