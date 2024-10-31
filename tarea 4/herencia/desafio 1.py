# Clase base Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def presentar(self):
        return f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}"

# Clase derivada Poeta
class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poema):
        super().__init__(nombre, nacionalidad)  # Llamada al constructor de la clase base
        self.tipo_poema = tipo_poema  # Atributo específico de la clase Poeta

    def presentar(self):
        base_presentar = super().presentar()  # Obtener la presentación del autor
        return f"{base_presentar}, Tipo de poesía: {self.tipo_poema}"

# Ejemplo de uso
poeta = Poeta("Pablo Neruda", "Chileno", "Amor")
print(poeta.presentar())
