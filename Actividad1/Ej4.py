#Ejercicio #4 Escribir un programa que determine si un número dado es par o impar.

numero = int(input("Ingrese un número para determinar si es par o impar: "))
if numero % 2 == 0: #Si su modulo es 0 es par
    print("El número ingresado es par")
else:
    print("El numero ingresado es impar")