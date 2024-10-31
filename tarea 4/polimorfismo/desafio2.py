# Clase base Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def biografia(self):
        return f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}."

# Clase derivada Escritor
class Escritor(Autor):
    def __init__(self, nombre, nacionalidad, genero_literario):
        super().__init__(nombre, nacionalidad)  # Inicializa la clase base
        self.genero_literario = genero_literario

    def biografia(self):
        base_biografia = super().biografia()  # Llama al método biografia de Autor
        return f"{base_biografia} Género literario: {self.genero_literario}."

# Ejemplo de uso
autor = Autor("Gabriel García Márquez", "Colombiano")
escritor = Escritor("Isabel Allende", "Chilena", "Ficción")

# Accediendo al método biografia de ambas clases
print(autor.biografia())  # Salida: Autor: Gabriel García Márquez, Nacionalidad: Colombiano.
print(escritor.biografia())  # Salida: Autor: Isabel Allende, Nacionalidad: Chilena. Género literario: Ficción.
