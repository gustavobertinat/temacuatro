class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre          # Atributo privado
        self.__nacionalidad = nacionalidad  # Atributo privado
        self.__libros = []              # Lista privada para almacenar libros

    # Método getter para el nombre
    def get_nombre(self):
        return self.__nombre

    # Método setter para el nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Método getter para la nacionalidad
    def get_nacionalidad(self):
        return self.__nacionalidad

    # Método setter para la nacionalidad
    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Método para agregar un libro a la lista
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    # Método para obtener la lista de libros
    def get_libros(self):
        return self.__libros

# Ejemplo de uso
autor1 = Autor("Gabriel García Márquez", "Colombiano")
autor1.agregar_libro("Cien años de soledad")
autor1.agregar_libro("El amor en los tiempos del cólera")

print(f"Autor: {autor1.get_nombre()}")
print("Libros escritos:")
for libro in autor1.get_libros():
    print(f"- {libro}")
