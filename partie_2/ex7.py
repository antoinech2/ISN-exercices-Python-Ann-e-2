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
# Paramètres: coordonnées (tupple de deux float), longeur de la ligne (integer), couleur (string (nom anglais) ou notation RGB), angle d'orientation du triangle (défaut: 0°)
def DrawLine(coords, length, pen_color, angle = 0):
    up()
    goto(coords)
    setheading(angle)
    color(pen_color)
    down()
    forward(length)


# Définition de la fonction DrawTriangle: Dessine un triangle
# Paramètres: coordonnées (tupple de deux float), longeur du côté (integer), couleur (string (nom anglais) ou notation RGB), angle d'orientation du triangle (défaut: 0°)
def DrawTriangle(coords, length, pen_color, angle = 0):
    up()
    goto(coords)
    setheading(angle)
    down()
    for cote in range (3):
        DrawLine(pos(), length, pen_color, heading())
        right(120)

# Définition de la fonction DrawHexagon: Dessine un hexagone
# Paramètres: coordonnées (tuple de deux float), longeur du côté (integer), couleur (string (nom anglais) ou notation RGB), angle d'orientation de l'hexagone (défaut: 0°)
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

def __main__():
    #Initialisation
    reset() #On supprime tout ce qu'il y a sur la fenêtre
    mode('logo') #On passe en mode logo pour obtenir des angles plus logiques (0° = nord)
    width(3) #On définit l'épaisseur du trait
    speed('fastest') #On définit la vitesse du dessin au maximum
    title('Mon dessin') #On définit un titre au dessin

    #Sol
    DrawLine((-200,-150), 400, "gray", 90)

    ##############
    #    VELO    #
    ##############

    #Roue droite
    DrawHexagon((0,-120), 30, "yellow")

    #Cadre du vélo droit
    DrawTriangle((0,-120), 68, "orange", -90)

    #Cadre du vélo gauche
    DrawTriangle((-68,-120), 68, "orange", -30)

    #Roue gauche
    DrawHexagon((-136,-120), 30, "yellow")

    #dernière ligne du cadre
    DrawLine((-136,-120), 68, "orange", 30)

    #Selle du vélo
    DrawLine((-102,-61), 30, "red", 50)

    #Guidon du vélo
    DrawLine((-34,-61), 30, "red", 50)
    DrawLine((-34,-40), 25, "red", 90)

    ##############
    #    ARBRE   #
    ##############

    #Tronc de l'arbre
    DrawLine((120,-150), 170, "brown")

    #Feuilles en haut de l'argre
    DrawHexagon((120,70), 50, "darkgreen")

    #Branche en bas à gauche
    DrawLine((120,-75), 30, "brown", -75)

    #Feuille en bas à gauche
    DrawHexagon((61,-59), 30, "darkgreen", -75)

    #Branche en haut à gauche
    DrawLine((120,-10), 30, "brown", -75)

    #Feuille en haut à gauche
    DrawHexagon((61,6), 30, "darkgreen", -75)

    ##############
    #   NUAGES   #
    ##############

    #Nuage en haut à droite
    DrawHexagon((-30,75), 15, "lightblue")

    #Nuage en bas à droite
    DrawHexagon((-55,30), 15, "lightblue")

    #Nuage du milieu
    DrawHexagon((-100,70), 15, "lightblue")

    #Nuage en bas à gauche
    DrawHexagon((-130,30), 15, "lightblue")

    #Nuage en haut à gauche
    DrawHexagon((-170,65), 15, "lightblue")

    hideturtle()


__main__()