"""
def suma(a, b):
    return a + b
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print(suma(num1, num2))

"""
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def modulo(a, b):
    return a % b
"""
def calculadora():
    print("Bienvenido a tu calculadora básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    
    opcion = input("Ingresa la opción (1/2/3/4/5): ")
    
    if opcion == '1':
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print(suma(num1, num2))
    elif opcion == '2':
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print(resta(num1, num2))
    elif opcion == '3':
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print(multiplicacion(num1, num2))
    elif opcion == '4':
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print(division(num1, num2))
    elif opcion == '5':
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print(modulo(num1, num2))
    else:
        print("Opción no válida.")

calculadora()
"""
def suma_3_valores(a, b,c):
    return a + b + c

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
print(suma_3_valores(num1, num2,num3))

