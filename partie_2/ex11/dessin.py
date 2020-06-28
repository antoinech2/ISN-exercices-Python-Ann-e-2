"ISN - Python - Partie 2 - Exercice 8"
"Programme qui affiche la table de multiplication d'un nombre en choisissant les bornes."

#######################################################
# Encodage: UTF-8                                     #
# Programme Python 3.7                                #
# Auteur : Antoine Cheucle                            #
# Pas de liscence, libre d'utilisation                #
# Dépendences: module Turtle, module dessin_tortue    #
#######################################################

#########################################
#Importation des modules externes:
from dessins_tortue import *
from turtle import *

#Corps principal du programme:
def __main__():
    #Initialisation
    reset() #On supprime tout ce qu'il y a sur la fenêtre
    mode('logo') #On passe en mode logo pour obtenir des angles plus logiques (0° = nord)
    width(1) #On définit l'épaisseur du trait
    speed('fastest') #On définit la vitesse du dessin au maximum
    title('Mon dessin') #On définit un titre au dessin
    up()
    goto(-250,0)

    size = 20

    for loop in range (5):
        DrawEtoile(size, "black", 90)
        fd(size+10)
        size+=10
    for loop in range (4):
        DrawEtoile(size, "black", 90)
        fd(size+10)
        size-=10

    exitonclick()

__main__()
