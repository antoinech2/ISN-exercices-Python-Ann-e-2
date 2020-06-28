"ISN - Python - Partie 2 - Exercice 9"
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

# Définition de la fonction DrawCarre: Dessine un carré
# Paramètres: taille (longeur du côté) (integer), couleur (string (nom anglais) ou notation RGB), angle d'orientation du triangle (défaut: 0°)
def DrawCarre(size, pen_color, angle = 0):
    color(pen_color)
    setheading(angle)
    down()
    for cote in range (4):
        fd(size)
        right(90)
    up()


# Définition de la fonction DrawTriangle: Dessine un triangle
# Paramètres: longeur du côté (integer), couleur (string (nom anglais) ou notation RGB), angle d'orientation du triangle (défaut: 0°)
def DrawTriangle(size, pen_color, angle = 0):
    color(pen_color)
    setheading(angle)
    down()
    for cote in range (3):
        fd(size)
        right(120)
    up()

# Définition de la fonction DrawTriangle: Dessine un triangle
# Paramètres: longeur du côté (integer), couleur (string (nom anglais) ou notation RGB), angle d'orientation du triangle (défaut: 0°)
def DrawEtoile(size, pen_color, angle = 0):
    color(pen_color)
    setheading(angle)
    down()
    for cote in range (5):
        fd(size)
        right(144)
    up()