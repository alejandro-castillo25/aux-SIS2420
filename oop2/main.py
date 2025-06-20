
# ? Variable names are in spanish, because... it says in the problem
# ? Igual es buena practica hacerlas en inglés

class Animal:
    # ? No estamos haciendo uso de los attributos, pero para futuro
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def emitir_sonido(self) -> None:
        print("Este animal hace un sonido :]")


class Perro(Animal):
    def emitir_sonido(self) -> None:
        print("Guau Guau!")


class Gato(Animal):
    def emitir_sonido(self) -> None:
        print("Miau!")


# ? No está bien hacer variables con caracteres especiales (ñ)
class Pajaro(Animal):
    def emitir_sonido(self) -> None:
        print("Pio Pio!")


def hacer_emitir_sonido(animales: list[Animal]) -> None:
    for animal in animales:
        animal.emitir_sonido()

# * Ejemplo de uso de la función:

if __name__ == "__main__":
    animals = [
        Perro("Toto", 3),
        Gato("Michi", 2),
        Pajaro("Belén", 5)
    ]

    hacer_emitir_sonido(animals)