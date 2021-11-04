#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici

from os import path # peremt de verifier chemin
from json import


# TODO: Définissez vos fonction ici

def recette_ex5(file_path):

    if path.exists(file_path): # if fichier exists, open n read
        with open(file_path, 'r') as f:
            recipes = json.load(f)   #open jason to stock file

    else: # creer nouveau fichier to store
        recipes = {}


    choice = input(
        'Choisissez une option \n a) Ajouter une recette \n b) '

    if choice =='d'
        print__recipe
    .strip()


    else:
        print('option non valide')

    with open(file_path, 'w') as f:
         json.dump(recipes, f)
    # loads info input into json file (saves input info)

    # pickle file also works, but harder to read



# rajouter save fichier pour save answers inputed (import path



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
