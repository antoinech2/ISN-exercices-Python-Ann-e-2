"ISN - Python - Partie 2 - Exercice 3"
"Programme qui affiche un carré de 100 pixel de côté, de contour vert et de fond rouge"
"Utilisation du module Turtle"

# Coding: UTF-8

#Programme Python 3.2
#Auteur : Antoine Cheucle
#Pas de liscence

#Importation de modules externes:

from turtle import *

reset()
color("green", "red")
begin_fill()
for i in range (4):
    forward(100)
    right(90)
end_fill()