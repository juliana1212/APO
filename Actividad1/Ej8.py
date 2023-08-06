#Ejercicio 8: Crear una función que invierta el orden de los elementos en una lista dada.
def invertir(lista):
    longitud = len(lista)
    for i in range(longitud // 2):
        lista[i], lista[longitud - i - 1] = lista[longitud - i - 1], lista[i]

listaoriginal = [10,20,30,40]
print("La lista original es:", listaoriginal)

invertir(listaoriginal)
print("La lista original invertida es:", listaoriginal)