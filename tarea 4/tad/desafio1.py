from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=14)  # 2 semanas
        self.devuelto = False

    def devolver_libro(self):
        self.devuelto = True
        self.libro.disponible = True

class Multa:
    def __init__(self, usuario, monto):
        self.usuario = usuario
        self.monto = monto
        self.pagada = False

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
        self.multas = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, isbn, id_usuario):
        libro = next((l for l in self.libros if l.isbn == isbn and l.disponible), None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            prestamo = Prestamo(libro, usuario)
            libro.disponible = False
            usuario.prestamos.append(prestamo)
            self.prestamos.append(prestamo)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("No se puede realizar el préstamo. Verifique la disponibilidad del libro y la existencia del usuario.")

    def devolver_libro(self, id_usuario, isbn):
        prestamo = next((p for p in self.prestamos if p.usuario.id_usuario == id_usuario and p.libro.isbn == isbn and not p.devuelto), None)

        if prestamo:
            prestamo.devolver_libro()
            print(f"Libro '{prestamo.libro.titulo}' devuelto por {prestamo.usuario.nombre}.")
            self.verificar_multa(prestamo)
        else:
            print("No se encontró el préstamo correspondiente.")

    def verificar_multa(self, prestamo):
        if datetime.now() > prestamo.fecha_devolucion:
            dias_retraso = (datetime.now() - prestamo.fecha_devolucion).days
            multa_monto = dias_retraso * 1.0  # 1.0 por día de retraso
            multa = Multa(prestamo.usuario, multa_monto)
            self.multas.append(multa)
            print(f"Se ha generado una multa de ${multa_monto} para {prestamo.usuario.nombre} por retraso.")

# Ejemplo de uso
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0451524935")
libro2 = Libro("1984", "George Orwell", "978-0451524936")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Agregar usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana García", "002")
biblioteca.agregar_usuario(usuario1)
biblioteca.agregar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("978-0451524935", "001")
biblioteca.devolver_libro("001", "978-0451524935")
