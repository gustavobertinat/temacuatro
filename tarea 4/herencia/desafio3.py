# Clase base Libro
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.año_publicacion}"

# Clase derivada LibroDigital
class LibroDigital(Libro):
    def __init__(self, titulo, autor, año_publicacion, formato, tamaño_archivo):
        super().__init__(titulo, autor, año_publicacion)  # Llamada al constructor de la clase base
        self.formato = formato  # Atributo específico de la clase LibroDigital
        self.tamaño_archivo = tamaño_archivo  # Atributo específico de la clase LibroDigital

    def mostrar_info(self):
        base_info = super().mostrar_info()  # Obtener la información del libro
        return f"{base_info}, Formato: {self.formato}, Tamaño de archivo: {self.tamaño_archivo} MB"

# Subclase EBook
class EBook(LibroDigital):
    def __init__(self, titulo, autor, año_publicacion, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, año_publicacion, formato, tamaño_archivo)  # Llamada al constructor de LibroDigital
        self.enlace_descarga = enlace_descarga  # Atributo específico de la clase EBook

    def mostrar_info(self):
        base_info = super().mostrar_info()  # Obtener la información del libro digital
        return f"{base_info}, Enlace de descarga: {self.enlace_descarga}"

# Ejemplo de uso
ebook = EBook("Cien años de soledad", "Gabriel García Márquez", 1967, "PDF", 2.5, "http://ejemplo.com/descarga")
print(ebook.mostrar_info())
