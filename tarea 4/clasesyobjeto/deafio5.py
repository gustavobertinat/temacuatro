class Biblioteca:
    def __init__(self):
        self.__autores = {}

    def agregar_autor(self, autor):
        if autor.nombre not in self.__autores:
            self.__autores[autor.nombre] = autor
        else:
            print(f"El autor {autor.nombre} ya está en la biblioteca.")

    def agregar_libro(self, nombre_autor, libro):
        if nombre_autor in self.__autores:
            self.__autores[nombre_autor].agregar_libro(libro)
        else:
            print(f"El autor {nombre_autor} no está en la biblioteca.")

    def buscar_libro_por_titulo(self, titulo):
        for autor in self.__autores.values():
            for libro in autor.obtener_libros():
                if libro.titulo.lower() == titulo.lower():
                    print(f"Libro encontrado: '{libro.titulo}' por {autor.nombre} (Género: {libro.genero}, ISBN: {libro.isbn})")
                    return libro
        print(f"El libro '{titulo}' no se encontró en la biblioteca.")
        return None

    def buscar_autor_por_nombre(self, nombre_autor):
        if nombre_autor in self.__autores:
            autor = self.__autores[nombre_autor]
            autor.imprimir_info()  # Usamos el método que ya imprime la info del autor
            return autor
        else:
            print(f"El autor '{nombre_autor}' no se encontró en la biblioteca.")
            return None

    def buscar_libros_por_genero(self, genero):
        libros_encontrados = []
        for autor in self.__autores.values():
            for libro in autor.obtener_libros():
                if libro.genero.lower() == genero.lower():
                    libros_encontrados.append(libro)
        if libros_encontrados:
            print(f"Libros encontrados en el género '{genero}':")
            for libro in libros_encontrados:
                print(f"- '{libro.titulo}' por {libro.autor} (ISBN: {libro.isbn})")
        else:
            print(f"No se encontraron libros en el género '{genero}'.")

# Ejemplo de uso
biblioteca = Biblioteca()

autor1 = Autor("Gabriel García Márquez", "Colombiano", datetime(1927, 3, 6), "Escritor colombiano.")
libro1 = Libro("Cien años de soledad", "Realismo mágico", "978-0451524935", autor1)
libro2 = Libro("El amor en los tiempos del cólera", "Romance", "978-0452273530", autor1)

biblioteca.agregar_autor(autor1)
biblioteca.agregar_libro("Gabriel García Márquez", libro1)
biblioteca.agregar_libro("Gabriel García Márquez", libro2)

# Buscar un libro por título
biblioteca.buscar_libro_por_titulo("Cien años de soledad")

# Buscar un autor por nombre
biblioteca.buscar_autor_por_nombre("Gabriel García Márquez")

# Buscar libros por género
biblioteca.buscar_libros_por_genero("Romance")
