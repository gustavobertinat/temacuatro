# Clase base Escritor
class Escritor:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def escribir(self):
        return f"{self.nombre} está escribiendo."

# Clase base Academico
class Academico:
    def __init__(self, institucion, area_expertise):
        self.institucion = institucion
        self.area_expertise = area_expertise

    def investigar(self):
        return f"{self.nombre} está investigando en el área de {self.area_expertise}."

# Clase derivada EscritorAcademico
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, institucion, area_expertise):
        Escritor.__init__(self, nombre, genero)  # Inicializar la clase Escritor
        Academico.__init__(self, institucion, area_expertise)  # Inicializar la clase Academico

    def publicar_articulo(self, titulo):
        return f"{self.nombre} ha publicado un artículo académico titulado: '{titulo}'."

# Ejemplo de uso
escritor_academico = EscritorAcademico("Ana Pérez", "Femenino", "Universidad Nacional", "Literatura Comparada")
print(escritor_academico.escribir())
print(escritor_academico.investigar())
print(escritor_academico.publicar_articulo("La influencia de la literatura en la sociedad"))
