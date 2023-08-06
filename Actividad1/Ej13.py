#13Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división
if __name__ == "__main__":
    print("Calculadora sencilla")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    if num2 != 0:
        division = num1 / num2
    else:
        division = "Error: No es posible dividir entre cero."

    print(f"\nSuma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")