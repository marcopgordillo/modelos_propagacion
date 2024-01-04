'''
Generate a Menu
'''
from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from examples import custom_style_2

modelos = {
    'prop_el': {
        'name': 'Propagación en el espacio libre',
        'options': [
            {
                'key': 1,
                'name': 'Free Space',
                'value': 2.0
            },
            {
                'key': 2,
                'name': 'Urban area cellular radio',
                'value': 3.5
            },
            {
                'key': 3,
                'name': 'Shadowed cellular radio',
                'value': 5.0
            },
            {
                'key': 4,
                'name': 'In building LOS',
                'value': 1.8
            },
            {
                'key': 5,
                'name': 'Obstructed in building',
                'value': 6.0
            },
            {
                'key': 6,
                'name': 'Obstructed in factories',
                'value': 3.0
            },
        ],

    },
    'ok_ha': {
        'name': 'Okumura-Hata',
        'options': [
            {
                'key': 1,
                'name': 'Ciudad pequeña o mediana',
                'value': 1
            },
            {
                'key': 2,
                'name': 'Gran ciudad',
                'value': 2
            },
            {
                'key': 3,
                'name': 'Zona suburbana',
                'value': 3
            },
            {
                'key': 4,
                'name': 'Area abierta o rural',
                'value': 4
            },
        ],
    },
}

def generate_options(data: dict) -> list:
    return [{'key': index + 1, 'name': value['name'], 'value': key} for index, (key, value) in enumerate(data.items())]

def get_ambiente_options(answers):
    return modelos[answers['modelo']]['options']

questions = [
    {
        'type': 'list',
        'name': 'modelo',
        'message': 'Que modelo desea utilizar?',
        'choices': generate_options(modelos),
    },
    {
        'type': 'list',
        'name': 'ambiente',
        'message': 'Seleccione el ambiente del modelo?',
        'choices': get_ambiente_options,
    },
]

def generate_a_menu():
    answers = prompt(questions, style=custom_style_2)
    return answers
