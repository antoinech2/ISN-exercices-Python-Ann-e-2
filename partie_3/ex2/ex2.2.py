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
    boucle = True
    while boucle:
        try:
            fichier_name = input("Entrez le chemin d'accès vers un fichier valide pour le lire\n")
            fichier = open(fichier_name, "r")
            boucle = False
        except:
            print("Fichier invalide! Entrez un chemin d'accès très valide!")
    donnees = fichier.readlines()
    fichier.close()
    fichier = open(input("Entrez le nom du nouveau fichier"), "a")
    print("Voici le contenu de votre fichier:")
    for loop in range (len(donnees)):
        data = donnees[loop].split("|")
        data.pop()
        print("Personne n°"+str(loop+1)+":\nNom: "+data[0]+"\nPrénom: "+data[1]+"\nAdresse: "+data[2]+"\nCode postal: "+data[3]+"\nVille: "+data[4]+"\nn° téléphone: "+data[5])
        data.append(input("Entrez l'année de naissance de cette personne:\n"))
        data.append(input("Entrez le sexe de cette personne:\n"))
        fichier.write("|".join(data)+"|\n")

__main__()
