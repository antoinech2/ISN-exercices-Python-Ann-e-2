#ISN - Python - Partie 1 - Exercice complémentaire
#Programme qui affiche les 20 premiers multiples de 7
#et qui affiche une "*" à coté de ceux qui sont multiples de 3

for nb in range (1,21):
    if (nb*7)%3 == 0:
        print(nb*7,"*",sep="", end=", ")
    else:
        print(nb*7,end=", ")

