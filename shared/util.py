# -*- coding: utf-8 -*-

from os import system, name

def clear():

    if name == 'int':
        _ = system('cls')
    else:
        _ = system('clear')