#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75],
                        "F": [0, 70]}

'NOTES'

# pour lire ligne par ligne,

def func():
    with open('text', 'r', encoding='utf-8') as f:
        liste_lignes = f.readlines()  # creates list of all content of file
        print(liste_lignes)

    # OR

    for line in f:
        print(line)

' CSV '
# POUR LIRE:
#    reader = csv_reader = csv.reader(csv_file, delimiter=',')

# POUR ÉCRIRE:
#    writer = csv.writer(csv_file, delimiter=',')
#    writer.writerow(['John'])


'JSON'

# POUR ÉCRIRE:
#    json.dump(x, f, indent=4)

' OS: fonction pour trouver chemin fichier'

# voir tableau avec fonctions

# TODO: Importez vos modules ici

import os
import sys

# TODO: Définissez vos fonctions ici

def compare(f1, f2):
    with open(f1, 'r', encoding='utf-8') as file1:
        with open(f2, 'r', encoding='utf-8') as file2:
            list_f1 = file1.read().split('\n')
            list_f2 = file2.read().split('\n')

            ligne = 0
            while ligne <= len(list_f1):
                if list_f1[ligne] == list_f2[ligne]:
                    ligne += 1
                else:
                    mot = 0
                    f1_line = list_f1[ligne].split(' ')
                    f2_line = list_f2[ligne].split(' ')
                    while mot <= len(list_f1[ligne]):
                        if f1_line[mot] == f2_line[mot]:
                            mot += 1
            print(f'la premiere différence est à la ligne {ligne} au mot {f1_line[mot]} ')

    f1.close()
    f2.close()


def note(f1, f2):
    with open(f1, 'r', encoding='utf-8') as file1:
        with open(f2, 'a', encoding='utf-8') as file2:
            f1_numbers = file1.readlines()

            for number in f1_numbers:
                for key in PERCENTAGE_TO_LETTER:
                    letter_range = range(PERCENTAGE_TO_LETTER[key][0], PERCENTAGE_TO_LETTER[key][0])
                    if number in letter_range:
                        file2.write(number + ':' + key + '\n')

    f1.close()
    f2.close()


def numbers(file):
    with open(file, 'r', encoding='utf-8') as f:
        f_list = f.read().split('\n')
        list_nombre = []
        for line in f_list:
            char_list = list(line.split(' '))
            for char in char_list:
                if char.isdigit():
                    list_nombre.append(int(char))

    return sorted(list_nombre, reverse=True)

if __name__ == '__main__':
    print(numbers('exemple.txt'))


