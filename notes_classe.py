#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import sys


# notes chap 8

# quand on lie document avec read(), le / est un char qui determine fin de ligne

# le deuxieme print(readlines) continue de lire where the first one left off

def read_text(path="./exemple.txt"):
    with open(path, "r", encoding='utf-8') as f:
        print(f.readlines())
        f.seek(0)  # on recommence le reader à la premiere ligne
        print(f.readlines()[0])


def write_json(path="./jason.txt"):
    couleur = {"lion": "ok"}


# sauvegarder dict => UTILISER JSON, À EXAMEN!!!!!


def write_pickle():
    couleur = {"lion": "bleh"}


# sauvegarder GROS fichier en binaire, diff avec json = pickle plus compact, tandis que json qd tu retourne dans json.txt,
# json.txt garde texte original + modification


if __name__ == '__main__':
    print(read_text("./exemple.txt"))

    # on peut lire et écrire en mettant dans with open(path, "r+", etc)
    # r+ = r et append (no squashing, old file is still there but u can write)
    # r + w = squashes (writes new) and reads

    print(os.getcwd())  # = get current working directory (find where ur file is)

    sys.stdout = open('./file.txt', 'w')
    print('test')
    print('ecrit dans un fichier')
    sys.stdout.close()

# si on veut print un nouveau text file pour tester nos print dans un gros code


PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75],
                        "F": [0, 70]}


# end NOTES CHAP8

