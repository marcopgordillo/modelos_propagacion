# -*- coding: utf-8 -*-

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
    '''
    Una función que genera el menu de opciones para elegir el modelo

    ...

    Parameters
    ----------
    data : dict
        Un diccionario que contiene información sobre los modelos, donde cada modelo tiene una clave de identificación

    Returns
    -------
    options : list
        Una lista de opciones de tipo diccionario que permite mostrar las opciones del menu

    '''
    return [{'key': index + 1, 'name': value['name'], 'value': key} for index, (key, value) in enumerate(data.items())]

def get_ambiente_options(answers) -> list:
    '''
    Retorna una lista de opciones del tipo ambiente que permite mostrar a Inquirer las opciones del menu de ambiente.

    ...    

    Parameters
    ----------
    answers : dict
        Un diccionario que contiene las respuestas previas elegidas por el usuario.
    
    Returns
    -------
    options : list
        Una lista de opciones de tipo diccionario que permite mostrar las opciones del menu

    '''

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
    '''
    Genera un menu con las opciones de modelo y ambiente a elegir

    ...

    Returns
    -------
    answers : dict
        Retorna un diccionario con las respuestas del usuario obtenidas desde la línea de comandos.
    '''
    return prompt(questions, style=custom_style_2)

def generate_exit_question():
    questions = [
        {
            'type': 'confirm',
            'message': '¿Desea continuar?',
            'name': 'continue',
            'default': True,
        },
    ]

    return prompt(questions, style=custom_style_2)