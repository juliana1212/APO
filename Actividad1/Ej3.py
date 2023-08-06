#Ejercicio #3 Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

longitud = int(input("Ingrese el tamaño de la lista: "))
min = int(input("Ingrese el valor mínimo de la lista: "))#Conocer el rango
max = int(input("Ingrese el valor máximo de la lista: "))

lista_aleatoria = [] #Se crea la lista 

for _ in range(longitud):#Hasta la longitud pedida
    numero_aleatorio = min + int(random.random() * (max - min + 1))
    lista_aleatoria.append(numero_aleatorio)

print("La lista con números aleatorios es:")
for numero in lista_aleatoria:
    print(numero)