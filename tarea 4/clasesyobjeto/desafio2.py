class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre          # Atributo privado
        self.__nacionalidad = nacionalidad  # Atributo privado
        self.__libros = []              # Lista privada para almacenar libros

    # Decorador @property para el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Método para agregar un libro a la lista
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    # Método para obtener la lista de libros
    def obtener_libros(self):
        return self.__libros.copy()

class Libro:
    def __init__(self, titulo, genero, isbn, autor):
        self.__titulo = titulo          # Atributo privado
        self.__genero = genero          # Atributo privado
        self.__isbn = isbn              # Atributo privado
        self.__autor = autor            # Atributo privado que referencia a un objeto Autor

        # Agregar el libro a la lista de libros del autor
        self.__autor.agregar_libro(self)

    # Decorador @property para el título
    @property
    def titulo(self):
        return self.__titulo

    # Decorador @property para el género
    @property
    def genero(self):
        return self.__genero

    # Decorador @property para el ISBN
    @property
    def isbn(self):
        return self.__isbn

    # Decorador @property para el autor
    @property
    def autor(self):
        return self.__autor.nombre  # Devolvemos el nombre del autor

# Ejemplo de uso
autor1 = Autor("Gabriel García Márquez", "Colombiano")
libro1 = Libro("Cien años de soledad", "Realismo mágico", "978-0451524935", autor1)
libro2 = Libro("El amor en los tiempos del cólera", "Romance", "978-0452273530", autor1)

print(f"Títulos de libros escritos por {autor1.nombre}:")
for libro in autor1.obtener_libros():
    print(f"- {libro.titulo} (Género: {libro.genero}, ISBN: {libro.isbn})")
