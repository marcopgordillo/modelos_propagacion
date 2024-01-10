#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.free_space import Free_space
from models.okumura_hata import Okumura_hata
from models.modelo import Modelo
from shared.menu_generator import generate_a_menu, modelos
from os import system

'''
Programa que permite calcular la pérdida en el espacio libre
'''

def main():
    while(True):
        print('Calculo de la pérdida en el espacio libre')
        answers = generate_a_menu()

        if answers['modelo'] == 'exit':
            break

        frecuencia = float(input('Ingrese la frecuencia (MHz): '))
        distancia = float(input('Ingrese la distancia (Km): '))
        
        if answers['modelo'] == 'prop_el':
            n = answers['ambiente']
            modelo: Modelo = Free_space(frecuencia, distancia, n)
        elif answers['modelo'] == 'ok_ha':
            ht = float(input('Ingrese la altura de TX (m): '))
            hr = float(input('Ingrese la altura de RX (m): '))
            ambiente = answers['ambiente']
            modelo: Modelo = Okumura_hata(frecuencia, distancia, ht, hr, ambiente)

        perdida = modelo.calcular_perdida()
        print(f"\nLa pérdida según el modelo {modelos[answers['modelo']]['name']} es: {perdida:4.2f}dB")
        input('Presione una tecla para continuar')
        system('cls')


if __name__ == "__main__":
    main()