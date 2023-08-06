#Ejericicio 7:Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

def minimo_maximo(lista):
    if not lista:
        return None, None 

    minimo = maximo = lista[0]

    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    return minimo, maximo

numeros = [30, 54, 65, 100, 45, 22, 3, 45, 65]

minimo, maximo = minimo_maximo(numeros)

print(f"El número más pequeño es: {minimo}")
print(f"El número más grande es: {maximo}")