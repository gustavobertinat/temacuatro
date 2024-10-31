class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []

    @property
    def nombre(self):
        return self.__nombre

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def obtener_libros(self):
        return self.__libros.copy()

class Libro:
    def __init__(self, titulo, genero, isbn, autor):
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__autor = autor
        self.__autor.agregar_libro(self)

    @property
    def titulo(self):
        return self.__titulo

    @property
    def genero(self):
        return self.__genero

    @property
    def isbn(self):
        return self.__isbn

    @property
    def autor(self):
        return self.__autor.nombre

class Biblioteca:
    def __init__(self):
        self.__autores = {}  # Diccionario para almacenar autores

    def agregar_autor(self, autor):
        if autor.nombre not in self.__autores:
            self.__autores[autor.nombre] = autor
        else:
            print(f"El autor {autor.nombre} ya está en la biblioteca.")

    def agregar_libro(self, nombre_autor, libro):
        if nombre_autor in self.__autores:
            self.__autores[nombre_autor].agregar_libro(libro)
        else:
            print(f"El autor {nombre_autor} no está en la biblioteca. Agrega primero al autor.")

    def listar_libros_por_autor(self, nombre_autor):
        if nombre_autor in self.__autores:
            libros = self.__autores[nombre_autor].obtener_libros()
            if libros:
                print(f"Libros de {nombre_autor}:")
                for libro in libros:
                    print(f"- {libro.titulo} (Género: {libro.genero}, ISBN: {libro.isbn})")
            else:
                print(f"{nombre_autor} no tiene libros registrados.")
        else:
            print(f"El autor {nombre_autor} no está en la biblioteca.")

# Ejemplo de uso
biblioteca = Biblioteca()

autor1 = Autor("Gabriel García Márquez", "Colombiano")
biblioteca.agregar_autor(autor1)

libro1 = Libro("Cien años de soledad", "Realismo mágico", "978-0451524935", autor1)
libro2 = Libro("El amor en los tiempos del cólera", "Romance", "978-0452273530", autor1)

biblioteca.agregar_libro("Gabriel García Márquez", libro1)
biblioteca.agregar_libro("Gabriel García Márquez", libro2)

biblioteca.listar_libros_por_autor("Gabriel García Márquez")
