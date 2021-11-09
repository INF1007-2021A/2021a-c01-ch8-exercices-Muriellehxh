#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici

import os
import sys

# TODO: Définissez vos fonctions ici

def comparaison(f1, f2):
    with open(f1, "r", encoding="utf-8") as fichier1:
        with open(f2, "r", encoding="utf-8") as fichier2:
            i = 0

            for line1 in fichier1:
                i += 1
                for line2 in fichier2:

                    if line1 == line2:
                        print('Ligne', i, ': est identique')
                    else:
                        print('Ligne', i, 'est différente')

            fichier1.close()
            fichier2.close()


def Triple(f1, f2):
    with open(f1, "r", encoding="utf-8") as fichier1, open(f2, "r", encoding="utf-8") as fichier2:

        for line in fichier1:
            for word in line:
                fichier2.write(word.ljust(3))





if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    f1 = 'fichier1.txt'
    f2 = 'fichier2.txt'
    print(comparaison(f1, f2))

