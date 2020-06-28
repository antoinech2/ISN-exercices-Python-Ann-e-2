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
    chosen_color = input("Entrez la couleur des carrés (Nom anglais)")
    chosen_size = float(input("Entrez la taille du côté des carrés (nombre positif)"))

    #Initialisation
    reset() #On supprime tout ce qu'il y a sur la fenêtre
    mode('logo') #On passe en mode logo pour obtenir des angles plus logiques (0° = nord)
    width(3) #On définit l'épaisseur du trait
    speed('fastest') #On définit la vitesse du dessin au maximum
    title('Mon dessin') #On définit un titre au dessin
    up()
    setheading(90)
    goto(-((chosen_size+20)*8)/2,-chosen_size/2)

    for loop in range (8):
        goto(xcor()+20+chosen_size,-chosen_size/2)
        DrawCarre(chosen_size, chosen_color)
        #setheading(90)


__main__()
