"ISN - Python - Partie 1 - Exercice 7"
#Programme qui détermine le nombre de lettres "e" dans une phrase/mot donnée.

#Lecture de l'entrée - On demande à l'utilisateur le mot/phrase la stocke dans la variable "phrase"
phrase=input("Entrez une phrase ou un mot.")

#Initialisation des variables
#On initialise la variable qui va servir à la boucle
boucle=0
#On initialise le compteur de lettre "e" à 0
compteur=0

#Boucle du nombre de caractères de l'entrée (Tant que la "boucle" est inférieure au nombre de caractères de la phrase donnée)
while(boucle<len(phrase)):
    #Si le caractère bouclé est un "e"
    if phrase[boucle] == "e":
        #On ajoute 1 au compteur de "e"
        compteur+=1
    #On incrémente le compteur de la boucle
    boucle+=1


#Après la boucle de tous les caractères, si il y a au moins un "e":
if compteur>0:
    #On affiche le nombre de "e"
    print('La chaîne de caractère contient la lettre "e"',compteur,"fois")
else:
    #Sinon on affiche qu'il n'y a pas de "e"
    print('La chaîne de caractère ne contient pas la lettre "e"')
