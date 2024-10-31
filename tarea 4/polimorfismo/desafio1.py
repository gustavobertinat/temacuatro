# Clase base Musico
class Musico:
    def instrumento(self):
        raise NotImplementedError("Este método debe ser sobrescrito por subclases")

# Subclase Guitarrista
class Guitarrista(Musico):
    def instrumento(self):
        return "Toco la guitarra."

# Subclase Baterista
class Baterista(Musico):
    def instrumento(self):
        return "Toco la batería."

# Función para demostrar el polimorfismo
def presentar_musico(musico):
    print(musico.instrumento())

# Ejemplo de uso
guitarrista = Guitarrista()
baterista = Baterista()

presentar_musico(guitarrista)  # Salida: Toco la guitarra.
presentar_musico(baterista)     # Salida: Toco la batería.
