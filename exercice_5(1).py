#ISN - Python - Partie 1 - Exercice 5
#Programme qui affiche une suite de 12 nombres dont chaque terme soit égal au triple du terme précédent .

#On demande à l'utilisateur la note en nombre flotant et on la stocke dans la variable "note"
nombre=int(input("Entrez le premier nombre de la liste."))

#On initialise la variable qui va servir à la boucle
boucle=1

#On boucle 12 fois:
while boucle<=12 :
    #On triple la valeur du nombre
    nombre=nombre*3
    #On affiche le nombre sans aller à la ligne
    print(nombre,end=", ")
    #On incrémente le compteur de la boucle
    boucle+=1
