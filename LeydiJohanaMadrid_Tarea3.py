def Suma(a,b):
    resultado= a + b
    return resultado

def Resta(a,b):
    resultado= a - b
    return resultado

def Multiplicacion(a,b):
    resultado= a * b
    return resultado

def Division(a,b):
    resultado= a / b
    return resultado

def Opciones():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


print("\n-----------CALCULADORA 📱-----------\n")



while True:

    Opciones()

    try:
        seleccionarOperacion= int(input("\n¿Qué operación deseas realizar 🤔?\n"))
    except:
        print("\n¡ERROR! 😕 Escoge una opción válida\n")
    
    if seleccionarOperacion == 1:
        print("\n---Sumar---😀\n")
        numeroUno= int(input("Digite el primer número: "))
        numeroDos= int(input("Digite el segundo número: "))
        resultadoOperacion=Suma(numeroUno,numeroDos)
        print(f"\nLa suma de los dos valores es: {resultadoOperacion}\n")

    if seleccionarOperacion == 2:
        print("\n---Restar---😀\n")
        numeroUno= int(input("Digite el primer número: "))
        numeroDos= int(input("Digite el segundo número: "))
        resultadoOperacion=Resta(numeroUno,numeroDos)
        print(f"\nLa resta de los dos valores es: {resultadoOperacion}\n")

    elif seleccionarOperacion == 3:
        print("\n---Multiplicar---😀\n")
        numeroUno= int(input("Digite el primer número: "))
        numeroDos= int(input("Digite el segundo número: "))
        resultadoOperacion=Multiplicacion(numeroUno,numeroDos)
        print(f"\nLa multiplicación de los dos valores es: {resultadoOperacion}\n")

    elif seleccionarOperacion == 4:
        print("\n---Dividir---😀\n")
        numeroUno= int(input("Digite el primer número: "))
        numeroDos= int(input("Digite el segundo número: "))
        resultadoOperacion=Division(numeroUno,numeroDos)
        print(f"\nLa división de los dos valores es: {resultadoOperacion}\n") 

    elif seleccionarOperacion == 5:
        print("\n---Saliste de la calculadora---😔\n")
        break
    else:
         print("\nOpción incorrecta 😐\n")
           



