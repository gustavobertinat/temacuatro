class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre          # Atributo privado
        self.__nacionalidad = nacionalidad  # Atributo privado
        self.__libros = []              # Lista privada para almacenar libros

    # Decorador @property para el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Decorador @property para el setter del nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Decorador @property para la nacionalidad
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Decorador @property para el setter de la nacionalidad
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad

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

print(f"Autor: {autor1.nombre}")  # Uso del getter
print(f"Nacionalidad: {autor1.nacionalidad}")  # Uso del getter

# Cambiando el nombre y la nacionalidad
autor1.nombre = "Gabriel García"
autor1.nacionalidad = "Colombiano - Nobel"

print(f"Nuevo nombre: {autor1.nombre}")  # Uso del getter
print(f"Nueva nacionalidad: {autor1.nacionalidad}")  # Uso del getter

print("Libros escritos:")
for libro in autor1.get_libros():
    print(f"- {libro}")
