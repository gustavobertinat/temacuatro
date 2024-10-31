class Habilidad:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def usar(self):
        print(f"Usando habilidad: {self.nombre} con poder {self.poder}.")

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habilidades = []

    def agregar_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def atacar(self):
        for habilidad in self.habilidades:
            habilidad.usar()

class Arma:
    def __init__(self, nombre, dano):
        self.nombre = nombre
        self.dano = dano

    def atacar(self):
        print(f"Atacando con el arma: {self.nombre}, causando {self.dano} de daño.")

class Juego:
    def __init__(self):
        self.personajes = {}
        self.armas = {}

    def agregar_personaje(self, personaje):
        self.personajes[personaje.nombre] = personaje

    def agregar_arma(self, arma):
        self.armas[arma.nombre] = arma

    def iniciar_batalla(self):
        print("¡La batalla ha comenzado!")
        # Aquí puedes implementar la lógica de batalla entre personajes y armas

# Ejemplo de uso
juego = Juego()

# Crear habilidades
habilidad_fuego = Habilidad("Rayo de Fuego", 30)
habilidad_hielo = Habilidad("Bola de Hielo", 25)

# Crear personajes
personaje1 = Personaje("Guerrero")
personaje1.agregar_habilidad(habilidad_fuego)
personaje1.agregar_habilidad(habilidad_hielo)

personaje2 = Personaje("Mago")
habilidad_terreno = Habilidad("Tierra Temblorosa", 20)
personaje2.agregar_habilidad(habilidad_terreno)

# Crear armas
arma1 = Arma("Espada Larga", 15)
arma2 = Arma("Bastón Mágico", 10)

# Agregar personajes y armas al juego
juego.agregar_personaje(personaje1)
juego.agregar_personaje(personaje2)
juego.agregar_arma(arma1)
juego.agregar_arma(arma2)

# Iniciar batalla
juego.iniciar_batalla()

# Ejemplo de ataque
personaje1.atacar()
