"ISN - Python - Partie 2 - Exercice 5"
"programme qui dessine des triangles équilatéraux tous de la même taille mais de couleurs différentes à des endroitsdifférents."

#########################################
# Encodage: UTF-8                       #
# Programme Python 3.7                  #
# Auteur : Antoine Cheucle              #
# Pas de liscence, libre d'utilisation  #
#########################################

# Importation des modules externes:
from turtle import *
from random import randint

# Définition des constantes:
long_cote = 100 #Taille du côté du triangle en pixel

# Définition des fonctions locales:

def DrawTriangle(pen_color):
    color(pen_color)
    down()
    for cote in range (3):
        fd(long_cote)
        right(240)
    up()

# Corps principal du programme :

reset()
speed("fastest")
colormode(255)
up()
width(5)

while True:
	goto(randint(-(window_width()/2),window_width()/2),randint(-(window_height()/2),window_height()/2))
	DrawTriangle((randint(0,255),randint(0,255),randint(0,255)))
	right(randint(0,359))
