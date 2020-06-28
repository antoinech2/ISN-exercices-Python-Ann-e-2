"ISN - Python - Partie 2 - Exercice 8"
"Programme qui affiche la table de multiplication d'un nombre en choisissant les bornes."

#########################################
# Encodage: UTF-8                       #
# Programme Python 3.7                  #
# Auteur : Antoine Cheucle              #
# Pas de liscence, libre d'utilisation  #
#########################################

#########################################
#Définition des fonctions locales:

def table(nombre, min, max):
    for loop in range (min, max+1):
        print(nombre,"x",loop,"=",nombre*loop,sep="")

#Corps principal du programme

nombre = int(input("Quelle table de multiplication voulez-vous afficher?"))
min = int(input("Quel est le premier nombre à multiplier?"))
max = int(input("Quel est le dernier nombre à multiplier?"))

table(nombre, min, max)