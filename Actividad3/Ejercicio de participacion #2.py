import math
#Numeral 1
class Vehículo:
    def __init__(self, velocidad_max, kilometraje):
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje
#Prueba
vehiculo = Vehículo(30, 10000)
print("La velocidad máxima es de:", vehiculo.velocidad_max)
print("El kilometraje es de:", vehiculo.kilometraje)

#Numeral 2 y 3
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Las coordenadas del punto son: ({self.x}, {self.y})")

    def mover(self, x, y):
        self.x = x
        self.y = y

# Prueba:
if __name__ == "__main__":
    p1 = Punto(10, 15)
    p1.mostrar()

    p1.mover(6, -4)
    p1.mostrar()
 #Numeral 4
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class rectángulo:
    def __init__(self, esquinainf_izq, esquinasup_der):
        self.esquinainf_izq = esquinainf_izq
        self.esquinasup_der = esquinasup_der

    def perímetro(self):
        base = abs(self.esquinasup_der.x - self.esquinainf_izq.x)
        altura = abs(self.esquinasup_der.y - self.esquinainf_izq.y)
        return 2 * (base + altura)

    def área(self):
        base = abs(self.esquinasup_der.x - self.esquinainf_izq.x)
        altura = abs(self.esquinasup_der.y - self.esquinainf_izq.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquinasup_der.x - self.esquinainf_izq.x)
        altura = abs(self.esquinasup_der.y - self.esquinainf_izq.y)
        return base == altura

# Prueba:
if __name__ == "__main__":
    punto1 = Punto(6, 8)
    punto2 = Punto(3, 3)

    rectangulo = rectángulo(punto1, punto2)
    print(f"El perímetro del rectángulo es de: {rectangulo.perímetro()}")
    print(f"El área del rectángulo es de: {rectangulo.área()}")

    if rectangulo.es_cuadrado():
        print("¡El rectángulo es un cuadrado!")
    else:
        print("¡El rectángulo no es un cuadrado!")
#Numeral 5
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Círculo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio**2
    
    def perímetro(self):
        return 2 * math.pi * self.radio
    
    def pertenece(self, punto):
        dcentro = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return dcentro <= self.radio
#Prueba

centro = Punto(5, 9)
circulo = Círculo(centro, 2)

area = circulo.area()
print("El Área del círculo es de:", area)

perímetro = circulo.perímetro()
print("El Perímetro del círculo es de:", perímetro)

punto = Punto(8, 6)
if circulo.pertenece(punto):
    print("El punto dado pertenece al círculo.")
else:
    print("El punto dado no pertenece al círculo.")
#Numeral 6
class Carta:
    
    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    ESPADA = "Espada"

    def __init__(self, valores, pinta):
        self.valor = valores
        self.pinta = pinta

#Prueba
if __name__ == "__main__":
    carta_1 = Carta(9, Carta.ESPADA)
    carta_2 = Carta(5, Carta.CORAZON)

    print(f"La carta 1: {carta_1.valor} de {carta_1.pinta}")
    print(f"La carta 2: {carta_2.valor} de {carta_2.pinta}")

#Numeral 7 al 11
class cuenta_bancaria:
    def __init__(self, ncuenta, propietarios, balance):
        self.ncuenta = ncuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        self.balance += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("El saldo insuficiente.")
    
    def cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
    
    def mostrar_detalles(self):
        print("El número de cuenta es :", self.ncuenta)
        print("Los propietarios de la cuenta son:", ', '.join(self.propietarios))
        print("El balance es:", self.balance)

# Prueba
cuenta = cuenta_bancaria("1000410154", ["Juliana", "Daniela"], 4000)
cuenta.mostrar_detalles()

cuenta.depositar(900)
cuenta.mostrar_detalles()

cuenta.retirar(100)
cuenta.mostrar_detalles()

cuenta.cuota_manejo()
cuenta.mostrar_detalles()
