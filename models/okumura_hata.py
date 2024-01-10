# -*- coding: utf-8 -*-

'''
Modelo Okumura-Hata
'''
import math
from models.modelo import Modelo

class Okumura_hata(Modelo):
    def __init__(self, frecuencia: float, distancia: float, ht: float, hr: float, ambiente: int) -> None:
        super().__init__(frecuencia, distancia)
        self.ht = ht
        self.hr = hr
        self.ambiente = ambiente

    def calcular_perdida(self) -> float:
        name_of_method = f"perdida_{str(self.ambiente)}"
        method = getattr(self, name_of_method, lambda: 'Give an input as 1 -5')
        return method()

    def perdida_1(self):
        Ahr = (1.1 * math.log10(self.frecuencia) - 0.7) * self.hr - (1.56 * math.log10(self.frecuencia) - 0.8)
        return self._perdida(Ahr) if self.frecuencia < 1500 else self._perdida_psc(Ahr)

    def perdida_2(self):
        if(self.frecuencia <= 300):
            Ahr = 8.29 * (math.log10(1.54 * self.hr)) ** 2 - 1.1
        else:
            Ahr = 3.2 * (math.log10(11.75 * self.hr)) ** 2 - 4.97

        return self._perdida(Ahr) if self.frecuencia < 1500 else self._perdida_psc(Ahr)

    def perdida_3(self):
        return self.perdida_1() - 2 * (math.log10(self.frecuencia/28)) ** 2 - 5.4

    def perdida_4(self):
        return self.perdida_1() - 4.78 * (math.log10(self.frecuencia)) ** 2 - 18.733 * math.log10(self.frecuencia) - 40.98

    def _perdida(self, Ahr):
        return 69.55 + 26.16 * math.log10(self.frecuencia) - 13.82 * math.log10(self.ht) - Ahr + (44.9 - 6.55 * math.log10(self.ht)) * math.log10(self.distancia)

    def _perdida_psc(self, Ahr):
        Cm = 3 if self.ambiente == 2 else 0
        return 46.3 + 33.9 * math.log10(self.frecuencia) - 13.82 * math.log10(self.ht) - Ahr + (44.9 - 6.55 * math.log10(self.ht)) * math.log10(self.distancia) + Cm
