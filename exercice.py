#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

