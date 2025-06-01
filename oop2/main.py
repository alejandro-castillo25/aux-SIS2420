
#? Variable names are in spanish, because... it says in the problem
#? Igual es buena practica hacerlas en inglés

class Animal:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def emitir_sonido(self) -> None:
        print("Este animal hace un sonido :]")



class Perro(Animal):
    def emitir_sonido(self) -> None:
            print("Guau Guau!")