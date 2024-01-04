'''
Interface, Abstract Class
'''
from abc import ABC, abstractmethod

class Modelo(ABC):

    def __init__(self, frecuencia: float, distancia: float) -> None:
        super().__init__()
        self.frecuencia = frecuencia
        self.distancia = distancia

    @abstractmethod
    def calcular_perdida():
        pass