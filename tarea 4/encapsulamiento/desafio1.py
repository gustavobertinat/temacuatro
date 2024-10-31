class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor    # Atributo privado
        self.__isbn = isbn      # Atributo privado

    # Método getter para el título
    def get_titulo(self):
        return self.__titulo

    # Método setter para el título
    def set_titulo(self, titulo):
        self.__titulo = titulo

    # Método getter para el autor
    def get_autor(self):
        return self.__autor

    # Método setter para el autor
    def set_autor(self, autor):
        self.__autor = autor

    # Método getter para el ISBN
    def get_isbn(self):
        return self.__isbn

    # Método setter para el ISBN
    def set_isbn(self, isbn):
        self.__isbn = isbn

# Ejemplo de uso
libro1 = Libro("1984", "George Orwell", "978-0451524935")
print(libro1.get_titulo())  # Salida: 1984
print(libro1.get_autor())    # Salida: George Orwell
print(libro1.get_isbn())      # Salida: 978-0451524935

# Cambiando el título
libro1.set_titulo("Rebelión en la granja")
print(libro1.get_titulo())  # Salida: Rebelión en la granja
