#Ejercicio 10: Escribir una función que calcule el factorial de un número dado.
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingrese un número el cual desea conocer su factorial: "))
resul = factorial(numero)
print(f"El factorial del {numero} es {resul}")