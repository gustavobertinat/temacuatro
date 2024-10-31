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

    # Método para obtener la lista de libros
    def obtener_libros(self):
        return self.__libros.copy()  # Devolvemos una copia de la lista para evitar modificaciones externas

    # Método para obtener la cantidad de libros
    def contar_libros(self):
        return len(self.__libros)

# Función para obtener el autor que ha escrito el mayor número de libros
def autor_con_mas_libros(lista_autores):
    if not lista_autores:  # Verificar si la lista está vacía
        return None

    autor_mas_libros = lista_autores[0]  # Inicializar con el primer autor
    max_libros = autor_mas_libros.contar_libros()

    for autor in lista_autores[1:]:
        num_libros = autor.contar_libros()
        if num_libros > max_libros:
            autor_mas_libros = autor
            max_libros = num_libros

    return autor_mas_libros

# Ejemplo de uso
autor1 = Autor("Gabriel García Márquez", "Colombiano")
autor1.agregar_libro("Cien años de soledad")
autor1.agregar_libro("El amor en los tiempos del cólera")

autor2 = Autor("J.K. Rowling", "Británica")
autor2.agregar_libro("Harry Potter y la piedra filosofal")
autor2.agregar_libro("Harry Potter y la cámara secreta")
autor2.agregar_libro("Harry Potter y el prisionero de Azkaban")

autor3 = Autor("Mario Vargas Llosa", "Peruano")
autor3.agregar_libro("La ciudad y los perros")

# Lista de autores
lista_autores = [autor1, autor2, autor3]

# Obtener el autor que ha escrito el mayor número de libros
autor_mas_productivo = autor_con_mas_libros(lista_autores)

if autor_mas_productivo:
    print(f"El autor que ha escrito el mayor número de libros es: {autor_mas_productivo.nombre} con {autor_mas_productivo.contar_libros()} libros.")
else:
    print("La lista de autores está vacía.")
