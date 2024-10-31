class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre          # Atributo privado
        self.__nacionalidad = nacionalidad  # Atributo privado
        self.__libros = []              # Lista privada para almacenar libros

    # Decorador @property para el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Decorador @property para la nacionalidad
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Método para agregar un libro a la lista
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    # Método para eliminar un libro de la lista
    def eliminar_libro(self, libro):
        try:
            self.__libros.remove(libro)
        except ValueError:
            print(f"El libro '{libro}' no se encuentra en la lista.")

    # Método para obtener la lista de libros
    def obtener_libros(self):
        return self.__libros.copy()  # Devolvemos una copia de la lista para evitar modificaciones externas

    # Método para contar la cantidad de libros
    def contar_libros(self):
        return len(self.__libros)

# Ejemplo de uso
autor1 = Autor("Gabriel García Márquez", "Colombiano")
autor1.agregar_libro("Cien años de soledad")
autor1.agregar_libro("El amor en los tiempos del cólera")

print(f"Libros de {autor1.nombre}: {autor1.obtener_libros()}")

# Agregar un libro
autor1.agregar_libro("El otoño del patriarca")
print(f"Libros de {autor1.nombre} tras agregar uno: {autor1.obtener_libros()}")

# Eliminar un libro
autor1.eliminar_libro("Cien años de soledad")
print(f"Libros de {autor1.nombre} tras eliminar uno: {autor1.obtener_libros()}")

# Intentar eliminar un libro que no existe
autor1.eliminar_libro("Cien años de soledad")
