# Clase base Usuario
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def presentar(self):
        return f"Usuario: {self.nombre}, Email: {self.email}"

# Clase derivada Bibliotecario
class Bibliotecario(Usuario):
    def __init__(self, nombre, email, seccion, años_experiencia):
        super().__init__(nombre, email)  # Llamada al constructor de la clase base
        self.seccion = seccion  # Atributo específico de la clase Bibliotecario
        self.años_experiencia = años_experiencia  # Atributo específico de la clase Bibliotecario

    def presentar(self):
        base_presentar = super().presentar()  # Obtener la presentación del usuario
        return f"{base_presentar}, Sección: {self.seccion}, Años de experiencia: {self.años_experiencia}"

# Ejemplo de uso
bibliotecario = Bibliotecario("María López", "maria.lopez@example.com", "Ficción", 5)
print(bibliotecario.presentar())
