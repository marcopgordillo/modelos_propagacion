'''
Menu modelo
'''
from shared.menu_generator import generate_a_menu

modelos = [
    {'id': 1, 'name': 'Propagación Espacio Libre'},
    {'id': 2, 'name': 'Okumura-Hata'},
]

def get_modelo() -> int:
    return generate_a_menu('Seleccione el modelo\n', modelos)