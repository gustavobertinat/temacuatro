# Clase base Empleado
class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado

    def presentar(self):
        return f"Empleado: {self.nombre}, ID: {self.id_empleado}"

# Clase para el rol Administrador
class Administrador:
    def __init__(self, nivel_acceso):
        self.nivel_acceso = nivel_acceso

    def gestionar(self):
        return f"Gestión a nivel: {self.nivel_acceso}"

# Clase para el rol Mantenimiento
class Mantenimiento:
    def realizar_mantenimiento(self):
        return "Realizando tareas de mantenimiento."

# Clase Gerente que hereda de Empleado y utiliza composición con Administrador
class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, nivel_acceso):
        super().__init__(nombre, id_empleado)  # Inicializar Empleado
        self.administrador = Administrador(nivel_acceso)  # Composición

    def presentar(self):
        return f"{super().presentar()}, {self.administrador.gestionar()}"

# Clase Tecnico que hereda de Empleado y utiliza composición con Mantenimiento
class Tecnico(Empleado):
    def __init__(self, nombre, id_empleado):
        super().__init__(nombre, id_empleado)  # Inicializar Empleado
        self.mantenimiento = Mantenimiento()  # Composición

    def presentar(self):
        return f"{super().presentar()}, {self.mantenimiento.realizar_mantenimiento()}"

# Clase Voluntario que hereda de Empleado
class Voluntario(Empleado):
    def __init__(self, nombre, id_empleado):
        super().__init__(nombre, id_empleado)  # Inicializar Empleado

    def presentar(self):
        return f"{super().presentar()}, Voluntario en la biblioteca."

# Ejemplo de uso
gerente = Gerente("Laura Martínez", 101, "Alto")
tecnico = Tecnico("Carlos Sánchez", 202)
voluntario = Voluntario("Ana Torres", 303)

print(gerente.presentar())
print(tecnico.presentar())
print(voluntario.presentar())
