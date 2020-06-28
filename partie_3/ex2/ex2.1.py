"ISN - Python - Partie 3 - Exercice 2.1"
"Ecrivez un script qui permette d'encoder un fichier texte dont les lignes contiendront\
    chacune les noms, prénom, adresse, code postal ,ville et n° de téléphone de différentes\
    personnes (considérez par exemple qu'il s'agit des membres d'un club)."

#######################################################
# Encodage: UTF-8                                     #
# Programme Python 3.7                                #
# Auteur : Antoine Cheucle                            #
# Pas de licence, libre d'utilisation                 #
# Dépendences: aucune                                 #
#######################################################

def __main__():
    fichier = open(input("Entrez le nom du fichier dans lequel écrire (N'oubliez pas d'inscrire également son extension s'il en possède une!)\n"), "a")
    print("Bien! Vous pouvez désormais commencer à entrer les données.")
    nb_personne = 0
    while True:
        nb_personne += 1
        donnees = []
        rep = input("Entrez le nom de famille de la personne n°"+str(nb_personne)+ " Appuyez sur Entrer pour annuler")
        if rep == "":
            break
        else:
            donnees.append(rep)
        donnees.append(input("Entrez le prénom de la personne n°"+str(nb_personne)))
        donnees.append(input("Entrez l'adresse de la personne n°"+str(nb_personne)))
        donnees.append(input("Entrez le code postal de la personne n°"+str(nb_personne)))
        donnees.append(input("Entrez la ville de la personne n°"+str(nb_personne)))
        donnees.append(input("Entrez le numéro de téléphone de la personne n°"+str(nb_personne)))
        fichier.write("|".join(donnees)+"|\n")
    fichier.close()
    print("Fin de l'éciture! Fichier sauvegardé.")


__main__()
