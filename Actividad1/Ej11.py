#Ejercicio 11: Crear un programa que genere una lista de números pares entre 1 y 100.
def lista_par():
    lista_par = [numero for numero in range(2, 101) if numero % 2 == 0]
    return lista_par

lpares_generada = lista_par()
print("La lista de números pares entre 1 y 100 es:")
print(lpares_generada)