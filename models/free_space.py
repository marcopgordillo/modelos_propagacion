'''
Model Free Space
'''
import math
from models.modelo import Modelo
from shared.menu_generator import generate_a_menu

environments = [
    {'id': 1, 'name': 'Free Space', 'n': 2.0},
    {'id': 2, 'name': 'Urban area cellular radio', 'n': 3.5},
    {'id': 3, 'name': 'Shadowed cellular radio', 'n': 5.0},
    {'id': 4, 'name': 'In building LOS', 'n': 1.8},
    {'id': 5, 'name': 'Obstructed in building', 'n': 6.0},
    {'id': 6, 'name': 'Obstructed in factories', 'n': 3.0},
]

class Free_space(Modelo):
    def __init__(self, frecuencia: float, distancia: float) -> None:
        super().__init__(frecuencia, distancia)
        self.n: float = 2.0

    def calcular_perdida(self) -> float:
        return 20 * math.log(self.frecuencia * 10**6, 10) + 10 * self.n * math.log(self.distancia * 10**3, 10) - 147.56

    def get_n(self) -> float:
        id = generate_a_menu("Seleccione el ambiente a calcular:", environments)

        value = list(filter(lambda x: x['id'] == id, environments))
        self.n = value[0]['n']
