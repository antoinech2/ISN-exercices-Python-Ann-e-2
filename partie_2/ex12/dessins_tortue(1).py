"ISN - Python - Partie 2 - Exercice 12"
"Programme qui contient les fonctions pour dessiner des formes prédéfinies (carré, triangle, étoile à 5 et 6 branches)."

#######################################################
# Encodage: UTF-8                                     #
# Programme Python 3.7                                #
# Auteur : Antoine Cheucle                            #
# Pas de liscence, libre d'utilisation                #
# Dépendences: module Turtle, module math             #
#######################################################

#########################################
#Importation des modules externes:
from turtle import *
from math import sqrt

#########################################
#Définition des fonctions locales:

# Définition de la fonction DrawSquare: Dessine un carré à la position de la tortue
# Paramètre: taille (longeur du côté) (integer)
def DrawSquare(size):
    down()
    for cote in range (4): #On répète 4 fois pour les 4 côtés
        fd(size)           #On avance de la taille pour tracer un côté
        right(90)          #On tourne de 90° (angle droit)
    up()


# Définition de la fonction DrawTriangle: Dessine un triangle à la position de la tortue
# Paramètres: taille (longeur du côté) (integer)
def DrawTriangle(size):
    down()
    for cote in range (3): #On répète 3 fois pour les 3 côtés
        fd(size)           #On avance de la taille pour tracer un côté
        right(120)         #On tourne de 120° (360/3)
    up()

# Définition de la fonction DrawStar5: Dessine une étoile à 5 branches à la position de la tortue
# Paramètres: taille (longeur du côté) (integer)
def DrawStar5(size):
    down()
    for cote in range (5): #On répète 5 fois pour les 5 côtés
        fd(size)           #On avance de la taille pour tracer un côté
        right(144)         #On tourne de 144° (360/5)
    up()

# Définition de la fonction DrawStar6: Dessine une étoile à 6 branches à la position de la tortue
# Paramètres: taille (longeur du côté) (integer)
def DrawStar6(size):        #L'étoile est composée de 6 triangles équilatéraux de sens opposés.
    DrawTriangle(size)      #On trace un premier triangle dans la direction de la tortue
    right(30)               #On tourne pour s'orienter vers le centre de l'étoile
    forward(size/sqrt(3))   #On avance jusu'au milieu (taille/racine de 3)
    left(120)               #On s'oriente vers le sommet de l'autre triangle (direction de la turtle perpendiculaire au côté du triangle actuel)
    forward(size/sqrt(3))   #On avance jusu'au sommet (taille/racine de 3)
    right(150)              #On s'oriente dans le bon sens pour tracer le triangle
    DrawTriangle(size)      #On trace le deuxième triangle
    #Note: l'orientation de la turtle est différente entre le premier et le deuxième triangle, ce qui applique l'angle sur la totalité de la figure.
    up()