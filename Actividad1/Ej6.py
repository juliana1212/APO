#Ejercicio #6 Crear un programa que calcule la suma de los números en una lista dada.

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma


lista = [1, 2, 3, 4, 5]


resultado_suma = suma_lista(lista)
print("La suma de todos los números de la lista es:", resultado_suma)