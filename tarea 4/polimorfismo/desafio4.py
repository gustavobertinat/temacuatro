import math

# Clase base Figura
class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por subclases")

# Subclase Circulo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)  # Área de un círculo: π * r²

# Subclase Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2  # Área de un cuadrado: lado²

# Función para mostrar el área de una figura
def mostrar_area(figura):
    print(f"El área es: {figura.area()}")

# Ejemplo de uso
circulo = Circulo(5)  # Crea un círculo con radio 5
cuadrado = Cuadrado(4)  # Crea un cuadrado con lado 4

# Muestra el área de cada figura
mostrar_area(circulo)  # Salida: El área es: 78.53981633974483
mostrar_area(cuadrado)  # Salida: El área es: 16
