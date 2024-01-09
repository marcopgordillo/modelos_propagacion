# -*- coding: utf-8 -*-

'''
Model Free Space
'''
import math
from models.modelo import Modelo

class Free_space(Modelo):
    def __init__(self, frecuencia: float, distancia: float, n: float) -> None:
        super().__init__(frecuencia, distancia)
        self.n = n

    def calcular_perdida(self) -> float:
        return 20 * math.log(self.frecuencia * 10**6, 10) + 10 * self.n * math.log(self.distancia * 10**3, 10) - 147.56
