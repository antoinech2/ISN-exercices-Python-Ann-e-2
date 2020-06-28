"ISN - Python - Partie 2 - Exercice 7"
"Programme qui affiche un dessin comportant un arbre, un vélo et des nuages en utilisant principalement des triangles avec le module Turtle"

#########################################
# Encodage: UTF-8                       #
# Programme Python 3.7                  #
# Auteur : Antoine Cheucle              #
# Pas de liscence, libre d'utilisation  #
#########################################

#########################################
# Importation des modules externes:
# Module Turtle pour l'affichage du dessin et les commandes de la tortue.
from turtle import *
#########################################

#########################################
#Définition des fonctions locales:

# Définition de la fonction DrawLine: Dessine une ligne droite
# Paramètres: coordonnées (tupple de deux float), longeur de la ligne (integer), couleur (string (nom anglais) ou notation RGB, angle d'orientation du triangle (défaut: 0°)
def DrawLine(coords, length, pen_color, angle = 0):
    up()
    goto(coords)
    setheading(angle)
    color(pen_color)
    down()
    forward(length)


# Définition de la fonction DrawTriangle: Dessine un triangle
# Paramètres: coordonnées (tupple de deux float), longeur du côté (integer), couleur (string (nom anglais) ou notation RGB, angle d'orientation du triangle (défaut: 0°)
def DrawTriangle(coords, length, pen_color, angle = 0):
    up()
    goto(coords)
    setheading(angle)
    down()
    for cote in range (3):
        DrawLine(pos(), length, pen_color, heading())
        right(120)

# Définition de la fonction DrawHexagon: Dessine un hexagone
# Paramètres: coordonnées (tuple de deux float), longeur du côté (integer), couleur (string (nom anglais) ou notation RGB, angle d'orientation de l'hexagone (défaut: 0°)
def DrawHexagon(coords, length, pen_color, angle = 0):
    up()
    goto(coords)
    setheading(angle)
    down()
    for cote in range (6):
        DrawTriangle(pos(), length, pen_color, heading())
        left(60)
    up()

#########################################
#Corps principal du programme

while True:

    #Initialisation
    reset()
    mode('logo')
    width(3)
    speed('fastest')
    title('Mon dessin')

    #Sol
    DrawLine((-200,0), 400, "gray", 90)

    ##############
    #    VELO    #
    ##############

    #Roue droite
    DrawHexagon((0,30), 30, "yellow")

    #Cadre du vélo droit
    DrawTriangle((0,30), 68, "orange", -90)

    #Cadre du vélo gauche
    DrawTriangle((-68,30), 68, "orange", -30)

    #Roue gauche
    DrawHexagon((-136,30), 30, "yellow")

    #dernière ligne du cadre
    DrawLine((-136,30), 68, "orange", 30)

    #Selle du vélo
    DrawLine((-102,89), 30, "red", 50)

    #Guidon du vélo
    DrawLine((-34,89), 30, "red", 50)
    DrawLine((-34,110), 25, "red", 90)

    ##############
    #    ARBRE   #
    ##############

    #Tronc de l'arbre
    DrawLine((120,0), 170, "brown")

    #Feuilles en haut de l'argre
    DrawHexagon((120,220), 50, "darkgreen")

    #Branche en bas à gauche
    DrawLine((120,75), 30, "brown", -75)

    #Feuille en bas à gauche
    DrawHexagon((61,91), 30, "darkgreen", -75)

    #Branche en haut à gauche
    DrawLine((120,140), 30, "brown", -75)

    #Feuille en haut à gauche
    DrawHexagon((61,156), 30, "darkgreen", -75)

    ##############
    #   NUAGES   #
    ##############

    #Nuage en haut à droite
    DrawHexagon((-30,225), 15, "lightblue")

    #Nuage en bas à droite
    DrawHexagon((-55,180), 15, "lightblue")

    #Nuage du milieu
    DrawHexagon((-100,220), 15, "lightblue")

    #Nuage en bas à gauche
    DrawHexagon((-125,180), 15, "lightblue")

    #Nuage en haut à gauche
    DrawHexagon((-170,215), 15, "lightblue")

hideturtle()
