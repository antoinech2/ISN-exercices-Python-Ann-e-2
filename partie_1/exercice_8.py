#ISN - Python - Partie 1 - Exercice 8
#Programme qui détermine si une chaine de caractère donnée est un palindrome,
#ou donne l'entrée avec les caractères inversés si ce n'est pas le cas.

#Lecture de l'entrée - On demande à l'utilisateur le mot/phrase la stocke dans la variable "phrase"
phrase=input("Entrez une phrase ou un mot:")

#Initialisation des variables
#On initialise la variable qui va servir à la boucle
boucle=0
#On initialise la variable qui va contenir le texte inversé
char_inverse=""

#Boucle du nombre de caractères de l'entrée
while(boucle<len(phrase)):
    #On ajoute le caractère à la variable du texte inversé; en partant de la fin du texte
    #On ajoute le caractère numéro boucle en partant de la fin du texte
    char_inverse=char_inverse+phrase[len(phrase)-1-boucle]
    #On incrémente le compteur de la boucle
    boucle+=1

#Après la boucle de tous les caractères, si le texte d'origine est identique au texte inversé:
if phrase == char_inverse:
    #On affiche que c'est un palindrome
    print("Votre phrase/mot est un palindrome:",phrase)
else:
    #Sinon on affiche le texte inversé
    print("Votre n'est pas un palindrome; Voici votre phrase/mot inversé(e):",char_inverse)
