# -*- coding: utf-8 -*-

'''
Interface, Abstract Class
'''
from abc import ABC, abstractmethod

class Modelo(ABC):
    '''
    Clase de tipo abstracta que permite instanciar una clase que la
    implementa para el tipo de modelo elegido

    ...

    Attributes
    ----------
    frecuencia : float
        Es la frecuencia de operación del radio enlace.
    distancia : float
        Es la distancia entre las antenas de Tx y Rx.

    Methods
    -------
    calcular_perdida()
        Clase abstracta. Calcula la pérdida del enlace en el espacio libre para un modelo dado.    
    '''

    def __init__(self, frecuencia: float, distancia: float) -> None:
        super().__init__()
        self.frecuencia = frecuencia
        self.distancia = distancia

    @abstractmethod
    def calcular_perdida():
        pass