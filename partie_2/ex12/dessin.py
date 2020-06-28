"ISN - Python - Partie 2 - Exercice 12"
"Programme qui affiche un dessin comportant ses carrés, triangles, étoiles à 5 et 6 branches."

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

def __main__(): #Définition de la fonction principale du programme
    #Initialisation
    reset() #On supprime tout ce qu'il y a sur la fenêtre
    width(1) #On définit l'épaisseur du trait
    speed('fastest') #On définit la vitesse de la tortue au maximum
    title('Mon magnifique dessin') #On définit un titre au dessin
    up()
    goto(0,200) #On ajuste la position de départ pour que le dessin soit centré à la fenêtre.

    size = 50 #On définit la taille initiale des figures (50 pixel)

    for loop in range (9): #On définit la suite de figures qui est répétée 9 fois
        DrawSquare(size)  #On trace un carré
        fd(size+7)       #On avance pour espacer un peu les figures
        DrawStar6(size) #On trace une étoile à 6 branches. C'est cette fonction qui applique l'angle qui fait "tourner" la figure
        fd(size+7)
        DrawTriangle(size) #On trace un triangle
        fd(size+7)
        DrawStar5(size) #Enfin, on trace l'étoi à 5 branches
        fd(size+7)
        size-=4   #On réduit la taille des figures de 4 pixel pour la prochaine suite d'instruction

    hideturtle() #On masque la tortue à la fin du dessin pour que le résultat corresponde à la consigne
    exitonclick() #On appelle cette fonction pour que la fenêtre se ferme lors du clic de l'utilisateur (permet à la fenêtre de rester ouverte)

__main__() #On appelle la fonction principale
