import math

'''
Programa que permite calcular la pérdida en el espacio libre
'''

environments = [
    {'id': 1, 'name': 'Free Space', 'n': 2.0},
    {'id': 2, 'name': 'Urban area cellular radio', 'n': 3.5},
    {'id': 3, 'name': 'Shadowed cellular radio', 'n': 5.0},
    {'id': 4, 'name': 'In building LOS', 'n': 1.8},
    {'id': 5, 'name': 'Obstructed in building', 'n': 6.0},
    {'id': 6, 'name': 'Obstructed in factories', 'n': 3.0},
]

def main():
    print('Calculo de la pérdida en el espacio libre')
    frecuencia = float(input('Ingrese la frecuencia (MHz): '))
    distancia = float(input('Ingrese la distancia (Km): '))
    
    n = get_n()
    perdida = calcular_perdida(frecuencia, distancia, n) 
    print(f"\nLa pérdida en el espacio libre es {perdida:4.2f}dB")

def calcular_perdida(frecuencia: float, distancia: float, n: float = 2.0):
    return 20 * math.log(frecuencia * 10**6, 10) + 10 * n * math.log(distancia * 10**3, 10) - 147.56

def get_n() -> float:
    n = 0

    text_array = [
        'Seleccione el ambiente a calcular\n', 
        *[f"{item['id']}. {item['name']}\n" for item in environments],
        '> ',
    ]

    while(n == 0):
        user_input = int(input("".join(text_array)))

        value = list(filter(lambda x: x['id'] == user_input, environments))
        n = value[0]['n'] if len(value) else 0

        if n == 0:
            print("Opción no disponible\n")

    return n

if __name__ == "__main__":
    main()
    exit()