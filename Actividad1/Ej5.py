#Ejercicio 5 Crear una función que convierta grados Fahrenheit a grados Celsius.

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit para convertir a: "))
celsius = fahrenheit_celsius(fahrenheit)

print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")
