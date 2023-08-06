#15Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.
def es_palindromo(cadena):
    # Convertimos la cadena a minúsculas y eliminamos los espacios en blanco
    cadena = cadena.lower().replace(" ", "")
    # Comparamos la cadena con su versión invertida
    if cadena == cadena[::-1]:
        return "Es un palíndromo."
    else:
        return "No es un palíndromo."

if __name__ == "__main__":
    texto = input("Ingresa una cadena de texto: ")
    resultado = es_palindromo(texto)
    print(resultado)