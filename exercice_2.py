#ISN - Python - Partie 1 - Exercice 2
#Programme qui affiche un message en fonction d'une note choisie par l'utilisateur

#On demande à l'utilisateur la note en nombre flotant et on la stocke dans la variable "note"
note=float(input("Entrez votre note sur 20:"))

#Si la note est plus petite que 1 ou plus grande que 20:
if note < 0 or note > 20:
	#La note n'est pas valide, on affiche un message.
    print("Note invalide. Entrez un nombre compris entre 0 et 20")
#Si la note est égale à 0:
elif note == 0:
	#On affiche "C'est lamentable"
    print("C'est lamentable!")
#Si la note est inférieure strictement à 10:
elif note < 10:
	#On affiche "C'est en dessous de la moyenne."
    print("C'est en dessous de la moyenne.")
#Si la note est comprise entre 10 et 20 non compris:
elif note < 20:
	#On affiche "J'ai la moyenne!"
    print("J'ai la moyenne!")
#Si la note est égale à 20:
elif note == 20:
	#On affiche "C'est excellent!"
    print("C'est excellent!")
