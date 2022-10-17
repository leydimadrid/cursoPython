textoEjercicio = "Python es un lenguaje de propósito general con un uso muy extendido. \
Esto hace que aunque algunos lenguajes tienen mejor posición, como es el caso de R \
en tecnologías de Data Science y Machine Learning, Python permite abarcar proyectos de \
una manera mucho más rápida y eficiente por lo que si eres desarrollador, ingeniero o \
científico de datos no deberías perder más tiempo y comenzar especializarte en Python o al menos conocer sus bondades."

textoEjercicio2 = textoEjercicio[250:300]
textoEjercicio3 = textoEjercicio2[2:10]


print("---Resultado---")

#1- Mostrar todo el texto en mayúscula.
print("1.")
print(textoEjercicio.upper())

#2- Mostrar el texto que hay entre la posición 20 a la 30.
print("2.")
print(textoEjercicio[20:30])

#3- Mostrar el texto que hay en la posición 150 a la 210 en minúsculas.
print("3.")
print(textoEjercicio[150:210].lower())

#Crear una segunda variable que contenga el texto anterior de la posición 250 a la 300 y convertirla en mayúscula.
print("4.")
print(textoEjercicio2.upper())

#Crear una tercera variable que contenga el texto de la segunda variable de la posicion 2 a la 10 y esta conviértala a minúscula.
print("5.")
print(textoEjercicio3.lower())

#Concatenación de la segunda y tercera variable.
print("6.")
print(textoEjercicio2.upper(),textoEjercicio3.lower())

