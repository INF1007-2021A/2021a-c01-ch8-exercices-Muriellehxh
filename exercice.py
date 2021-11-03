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


# TODO: Importez vos modules ici

import os
import sys

# TODO: Définissez vos fonction ici

f1_list = []
f2_list = []

def comparaison_2_fichiers(f1, f2):
    with open(f1, 'r') as f1_read:
        for line in f1_read:
            for ch in line:
                f1_list.append(ch)

    with open(f2, 'r') as f2_read:
        for ligne in f2_read:
            for mn in ligne:
                f2_list.append(mn)

    if f1_list == f2_list:
        print('listes sont les memes')


    else:
        if len(f1_list) < len(f2_list):
            return f2_list[f1_list.index(f1_list[-1]) + 1]
        if len(f2_list) < len(f1_list):
            return f1_list[f2_list.index(f2_list[-1]) + 1]

        if len(f1_list) == len(f2_list):
            for n in range(len(f1_list)):
                if f1_list[n] != f2_list[n]:
                   return f1_list[n], f2_list[n]


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    f1 = 'fichier1.txt'
    f2 = 'fichier2.txt'
    print(comparaison_2_fichiers(f1, f2))

