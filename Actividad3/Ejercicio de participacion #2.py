class Vehículo:
    def _init_(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

# Ejemplo de uso
vehiculo = Vehículo(200, 15000)
print("Velocidad máxima:", vehiculo.velocidad_maxima)
print("Kilometraje:", vehiculo.kilometraje)