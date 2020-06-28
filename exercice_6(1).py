#ISN - Python - Partie 1 - Exercice 6
#Programme qui affiche des "*", avec une "*" de plus a chaque ligne, 7 fois.
#Résultat attendu:
#*
#**
#***
#****
#*****
#******
#*******

#On initialise la variable qui va servir à la boucle
boucle=1

#On définit le premier caractère à afficher
etoile="*"

#On boucle 7 fois
while boucle<=7 :
    #On affiche le résultat
    print(etoile)
    #On ajoute une étoile dans la chaine de caractère pour la prochaine boucle
    etoile=etoile+"*"
    #On incrémente le compteur de la boucle
    boucle+=1
