# Clase base Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descripcion(self):
        return f"Título: '{self.titulo}', Autor: {self.autor}"

# Subclase LibroEspecializado
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        super().__init__(titulo, autor)  # Inicializa la clase base
        self.campo_estudio = campo_estudio  # Atributo específico
        self.nivel_especializacion = nivel_especializacion  # Atributo específico

    def descripcion(self):
        base_descripcion = super().descripcion()  # Llama al método de la clase base
        return f"{base_descripcion}, Campo de estudio: {self.campo_estudio}, Nivel de especialización: {self.nivel_especializacion}."

# Ejemplo de uso
libro = Libro("Introducción a la Programación", "John Doe")
libro_especializado = LibroEspecializado("Análisis de Algoritmos", "Jane Smith", "Informática", "Avanzado")

# Mostrando descripciones
print(libro.descripcion())  # Salida: Título: 'Introducción a la Programación', Autor: John Doe
print(libro_especializado.descripcion())  # Salida: Título: 'Análisis de Algoritmos', Autor: Jane Smith, Campo de estudio: Informática, Nivel de especialización: Avanzado.
