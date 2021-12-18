#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75],
                        "F": [0, 70]}


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
    with open(f1, "r", encoding="utf-8") as fichier1, open(f2, "a", encoding="utf-8") as fichier2:

        for line in fichier1:
                for word in line.split():

                   fichier2.write(word + '   ')

# a permet d'ajouter dans un fichier --> en crée un si ça existe pas encore


def Note(f1, f2):
    with open(f1, "r", encoding="utf-8") as fichier1, open(f2, "a", encoding="utf-8") as fichier2:

            for grade in fichier1:
                grade = (grade.strip('\n'))
                for letter in PERCENTAGE_TO_LETTER:

                    if int(grade) in range(PERCENTAGE_TO_LETTER[letter][0], PERCENTAGE_TO_LETTER[letter][1]):
                        fichier2.write(grade + ' ' + letter + "\n")

# when there's one word in line, NO NEED to put 2 for loops to get single word in line
# when u wanna refer to index and element in dictionary in for loop, JUST refer to index, after refer to value with dict[index]

# CHECK IF INT or BOOl !! (type of value)
# when u want to go ton next line: + '\n' <== backslash!!


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    f1 = 'fichier1.txt'
    f2 = 'fichier2'
    print(comparaison(f1, f2))

    print(Triple(f1, f2))

    notes = 'notes.txt'
    f3 = 'fichier3.txt'
    print(Note(notes, f3))