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
    seleccionarOperacion= int(input("\n¿Qué operación deseas realizar 🤔?\n"))
    

    
    if seleccionarOperacion == 1: 
        numeroUno= int(input("😀 Digite el primer número: "))
        numeroDos= int(input("😀 Digite el segundo número: "))
        resultadoOperacion=Suma(numeroUno,numeroDos)
        print(f"\n➕ La suma de los dos valores es: {resultadoOperacion}\n")

    if seleccionarOperacion == 2:
            numeroUno= int(input("😀 Digite el primer número: "))
            numeroDos= int(input("😀 Digite el segundo número: "))
            resultadoOperacion=Resta(numeroUno,numeroDos)
            print(f"\n➖ La resta de los dos valores es: {resultadoOperacion}\n")

    if seleccionarOperacion == 3:
            numeroUno= int(input("😀 Digite el primer número: "))
            numeroDos= int(input("😀 Digite el segundo número: "))
            resultadoOperacion=Multiplicacion(numeroUno,numeroDos)
            print(f"\n✖ La multiplicación de los dos valores es: {resultadoOperacion}\n")

    if seleccionarOperacion == 4:
            numeroUno= int(input("😀 Digite el primer número: "))
            numeroDos= int(input("😀 Digite el segundo número: "))
            resultadoOperacion=Division(numeroUno,numeroDos)
            print(f"\n➗ La división de los dos valores es: {resultadoOperacion}\n") 

    if seleccionarOperacion == 5:
            print("\n---¡Hasta luego!👋 Has salido de la calculadora---😔\n")
            break

           



