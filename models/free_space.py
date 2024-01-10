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
        return 20 * math.log10(self.frecuencia * 10**6) + 10 * self.n * math.log10(self.distancia * 10**3) - 147.56
