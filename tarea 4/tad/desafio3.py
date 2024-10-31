class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio}, Cantidad: {self.cantidad}"

class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado

    def __str__(self):
        return f"Empleado: {self.nombre} (ID: {self.id_empleado})"

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}
        self.empleados = {}

    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto

    def agregar_empleado(self, empleado):
        self.empleados[empleado.id_empleado] = empleado

    def listar_productos(self):
        print(f"Productos en {self.nombre}:")
        for producto in self.productos.values():
            print(producto)

class Transaccion:
    def __init__(self, tienda, empleado, producto, cantidad):
        self.tienda = tienda
        self.empleado = empleado
        self.producto = producto
        self.cantidad = cantidad
        self.total = producto.precio * cantidad

class Inventario:
    def __init__(self):
        self.tiendas = {}

    def agregar_tienda(self, tienda):
        self.tiendas[tienda.nombre] = tienda

    def realizar_transaccion(self, nombre_tienda, id_empleado, nombre_producto, cantidad):
        tienda = self.tiendas.get(nombre_tienda)
        empleado = tienda.empleados.get(id_empleado) if tienda else None
        producto = tienda.productos.get(nombre_producto) if tienda else None

        if tienda and empleado and producto and producto.cantidad >= cantidad:
            transaccion = Transaccion(tienda, empleado, producto, cantidad)
            producto.cantidad -= cantidad  # Actualiza la cantidad de producto
            print(f"Transacción realizada: {transaccion.cantidad} x {transaccion.producto.nombre} en {tienda.nombre} por {empleado.nombre}. Total: ${transaccion.total}")
        else:
            print("Error en la transacción. Verifica los datos.")

# Ejemplo de uso
inventario = Inventario()

# Crear tiendas
tienda1 = Tienda("Tienda A")
tienda2 = Tienda("Tienda B")

# Agregar productos
producto1 = Producto("Camiseta", 20.00, 100)
producto2 = Producto("Pantalón", 30.00, 50)

tienda1.agregar_producto(producto1)
tienda1.agregar_producto(producto2)

# Agregar empleados
empleado1 = Empleado("Juan Pérez", "001")
empleado2 = Empleado("Ana García", "002")

tienda1.agregar_empleado(empleado1)
tienda1.agregar_empleado(empleado2)

# Agregar tiendas al inventario
inventario.agregar_tienda(tienda1)
inventario.agregar_tienda(tienda2)

# Listar productos en tienda
tienda1.listar_productos()

# Realizar una transacción
inventario.realizar_transaccion("Tienda A", "001", "Camiseta", 2)

# Verificar cantidad de producto después de la transacción
tienda1.listar_productos()
