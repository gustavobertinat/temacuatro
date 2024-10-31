# Clase base Operacion
class Operacion:
    def resultado(self):
        raise NotImplementedError("Este método debe ser sobrescrito por subclases")

# Subclase Suma
class Suma(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def resultado(self):
        return self.a + self.b  # Realiza la suma

# Subclase Multiplicacion
class Multiplicacion(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def resultado(self):
        return self.a * self.b  # Realiza la multiplicación

# Función para mostrar el resultado de una operación
def mostrar_resultado(operacion):
    print(f"El resultado es: {operacion.resultado()}")

# Ejemplo de uso
suma = Suma(5, 3)  # Crea una operación de suma
multiplicacion = Multiplicacion(4, 2)  # Crea una operación de multiplicación

# Muestra el resultado de cada operación
mostrar_resultado(suma)          # Salida: El resultado es: 8
mostrar_resultado(multiplicacion)  # Salida: El resultado es: 8
