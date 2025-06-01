from math import inf
#! Este trabajo se revisó en privado, por eso no tiene sus commits

def is_capicua(num: int) -> bool:
    n = num
    temp = 0
    while (n != 0):
        temp = (n % 10) + (temp * 10)
        n //= 10
    return temp == num


# Una vez me anularon mi parcial por hacer así
def fibonnaci(n: int):
    fibo = [0, 1]

    for i in range(2, n + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    return fibo[n - 1]


def count_chars(text: str) -> dict:
    dic = {}

    for ch in text:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

    return dic


# ? Esto es para los divisores, la functión del num perfecto depende de esto :>
def get_divisors(n: int) -> list[int]:
    return [i for i in range(1, (n // 2) + 2) if n % i == 0]


def is_perfect_num(n: int) -> bool:
    return sum(get_divisors(n)) == n  # trucazo no?


def multiply_matrices(m_a: list[list[int]], m_b: list[list[int]]):
    row_a = len(m_a)
    col_a = len(m_a[0])

    row_b = len(m_b)
    col_b = len(m_b[0])

    if (col_a != row_b):
        # ? Inglés es buena práctica
        raise ValueError(
            'The columns of Matrix A must have the same number as the rows of Matrix B')

    res: list[list[int]] = [[0 for _ in range(row_a)] for _ in range(col_b)]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                res[i][j] += m_a[i][k] + m_b[k][j]

    return res


# print(multiply_matrices(
#     [
#         [1],
#         [3]
#     ],
#     [
#         [4, 5]
#     ]
# ))


# Este ya es más bonito
def get_max_2x2sum(matrix: list[list[int]]) -> int:

    if (len(matrix) < 2 or len(matrix[0]) < 2):
        raise ValueError('The matrix dimensions are not right (less than 2)')

    ans = int(-inf)

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            ans = max(ans, matrix[i][j] + matrix[i+1][j] +
                      matrix[i][j + 1] + matrix[i + 1][j + 1])

    return ans


# El problema me da los nombres de los items
# Asi que le haré caso aunque no sea bueno hacerlo en español
class Estudiante:
    def __init__(self, nombre: str, notas: list[float]):
        self.nombre = nombre
        self.notas = notas

    def promedio(self) -> float:
        return sum(self.notas) / len(self.notas)

    def aprobado(self) -> bool:
        return self.promedio() >= 60

# * Uso:
# student = Estudiante("Fernando", [23, 51, 45, 56, 100, 100])
# print(student.promedio())

# ? Estoy mutando el salario_sabe, porque el problema no me pide explicitamente getters


class Empleado:
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario_total(self):
        return self.salario_base


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_base: float):
        super().__init__(nombre, salario_base + salario_base*0.2)


class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre: str, salario_base: float):
        super().__init__(nombre, salario_base + salario_base*0.1)

# * Uso:
# empl1 = Empleado("Pepe", 1500.0)
# empl2 = EmpleadoTiempoCompleto("Juan", 1500.0)
# empl3 = EmpleadoMedioTiempo("Belén", 1500.0)

# print(empl1.calcular_salario_total())
# print(empl2.calcular_salario_total())
# print(empl3.calcular_salario_total())


class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')


class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, puertas: int):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def describir(self):
        super().describir()
        print(f'Puertas: {self.puertas}')


class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, cilindrada: bool):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def describir(self):
        super().describir()
        print(f'Cilindrada: {'Sí' if self.cilindrada else 'No'}')


# * Uso:

# vehiculo = Vehiculo("Tesla", "A")
# vehiculo.describir()
# print('------') # Esto para que decorar

# auto = Auto("Toyota", "V", 4)
# auto.describir()
# print('------')

# moto = Moto("Aurora", "A1", False)
# moto.describir()
