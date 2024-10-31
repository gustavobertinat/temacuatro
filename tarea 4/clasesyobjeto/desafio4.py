from datetime import datetime

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, biografia=""):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__fecha_nacimiento = fecha_nacimiento  # Almacenar como objeto datetime
        self.__biografia = biografia
        self.__libros = []
        self.__premios = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @property
    def biografia(self):
        return self.__biografia

    @biografia.setter
    def biografia(self, nueva_biografia):
        self.__biografia = nueva_biografia

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def eliminar_libro(self, libro):
        try:
            self.__libros.remove(libro)
        except ValueError:
            print(f"El libro '{libro.titulo}' no se encuentra en la lista.")

    def agregar_premio(self, premio):
        self.__premios.append(premio)

    def listar_premios(self):
        return self.__premios.copy()

    def calcular_edad(self):
        hoy = datetime.now()
        edad = hoy.year - self.__fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day):
            edad -= 1
        return edad

    def imprimir_info(self):
        print(f"Autor: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de Nacimiento: {self.__fecha_nacimiento.strftime('%d/%m/%Y')}")
        print(f"Edad: {self.calcular_edad()} años")
        print(f"Biografía: {self.biografia}")
        print("Libros escritos:")
        for libro in self.__libros:
            print(f"- {libro.titulo}")
        print("Premios:")
        for premio in self.__premios:
            print(f"- {premio}")

# Ejemplo de uso
autor1 = Autor("Gabriel García Márquez", "Colombiano", datetime(1927, 3, 6), "Escritor colombiano, conocido por su obra en el realismo mágico.")
autor1.agregar_libro("Cien años de soledad")
autor1.agregar_libro("El amor en los tiempos del cólera")
autor1.agregar_premio("Premio Nobel de Literatura 1982")

autor1.imprimir_info()
