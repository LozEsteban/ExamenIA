from suma import sumar
from resta import restar
from Multiplicacion import multiplicar
from dividir import dividir

# Interfaz:
print("Seleccione una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

operacion = input("Ingresa el número de la operación deseada (1/2/3/4): ")

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Ejecución
if operacion == '1':
    print(f"{numero1} + {numero2} = {sumar(numero1, numero2)}")

elif operacion == '2':
    print(f"{numero1} - {numero2} = {restar(numero1, numero2)}")

elif operacion == '3':
    print(f"{numero1} * {numero2} = {multiplicar(numero1, numero2)}")

elif operacion == '4':
    resultado = dividir(numero1, numero2)
    if resultado != "Error: División por cero":
        print(f"{numero1} / {numero2} = {resultado}")
    else:
        print(resultado)

else:
    print("Operación no válida")
