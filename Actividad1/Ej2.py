#Ejercicio #2: Escribir una función que calcule el área de un círculo dado su radio.
def area_circulo(radio):
    area = 3.141592653589793 * (radio ** 2)
    return area

radioc = (int(input("Ingrese el radio del circulo para calcular el area:")))
area_circulo = area_circulo(radioc)
print("El área del círculo de radio",radioc, "es:", area_circulo)