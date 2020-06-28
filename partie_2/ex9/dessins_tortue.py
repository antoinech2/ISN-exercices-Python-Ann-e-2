"ISN - Python - Partie 2 - Exercice 8"
"Programme qui contient les fonctions pour dessiner des formes (carré)."

#######################################################
# Encodage: UTF-8                                     #
# Programme Python 3.7                                #
# Auteur : Antoine Cheucle                            #
# Pas de liscence, libre d'utilisation                #
# Dépendences: module Turtle                          #
#######################################################

#########################################
#Importation des modules externes:
from turtle import *

#########################################
#Définition des fonctions locales:

def DrawCarre(size, pen_color):
    color(pen_color)
    down()
    for cote in range (4):
        fd(size)
        right(90)
    up()