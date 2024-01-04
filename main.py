from models.free_space import Free_space
from models.menu_modelo import get_modelo, modelos
from models.okumura_hata import Okumura_hata
from models.modelo import Modelo

'''
Programa que permite calcular la pérdida en el espacio libre
'''

def main():
    print('Calculo de la pérdida en el espacio libre')

    # Elegir el modelo
    modelo_id = get_modelo()

    frecuencia = float(input('Ingrese la frecuencia (MHz): '))
    distancia = float(input('Ingrese la distancia (Km): '))
    
    if modelo_id == 1:
        modelo: Modelo = Free_space(frecuencia, distancia)
        modelo.get_n()
    elif modelo_id == 2:
        ht = float(input('Ingrese la altura de TX (m): '))
        hr = float(input('Ingrese la altura de RX (m): '))
        modelo: Modelo = Okumura_hata(frecuencia, distancia, ht, hr)
        modelo.get_ambiente()
    
    perdida = modelo.calcular_perdida()
    modelo_selected = list(filter(lambda x: x['id'] == modelo_id, modelos))
    print(f"\nLa pérdida según el modelo {modelo_selected[0]['name']} es: {perdida:4.2f}dB")


if __name__ == "__main__":
    main()
    exit()