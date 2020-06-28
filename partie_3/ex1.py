"ISN - Python - Partie 3 - Exercice 1"
"Ecrivez un script qui permette de créer et de relire aisément un fichier texte. Votre\
    programme demandera d'abord à l'utilisateur d'entrer le nom du fichier. Ensuite il lui\
    proposera le choix, soit d'enregistrer de nouvelles lignes de texte, soit d'afficher le\
    contenu du fichier. L'utilisateur devra pouvoir entrer ses lignes de texte successives en   \
    utilisant simplement la touche <Enter> pour les séparer les unes des autres. Pour\
    terminer les entrées, il lui suffira d'entrer une ligne vide (c'est-à-dire utiliser la touche  \
    <Enter> seule).L'affichage du contenu devra montrer les lignes du fichier séparées les  \
    unes des autres de la manière la plus naturelle (les codes de fin de ligne ne doivent pas\
    apparaitre)."

#######################################################
# Encodage: UTF-8                                     #
# Programme Python 3.7                                #
# Auteur : Antoine Cheucle                            #
# Pas de licence, libre d'utilisation                 #
# Dépendences: aucune                                 #
#######################################################

def __main__():
	answer = ""
	while answer not in ["E","e","L","l","Q","q"]:
		answer = input("Bonjour ! Que voulez-faire ?\nTapez 'E' pour écrire de nouvelles lignes de texte.\nTapez 'Q' pour quitter.\nTapez 'L' pour lire vos oeuvres.\n")
	if answer in ["Q","q"]:
		return
	elif answer in ["E","e"]:
		fichier = open(input("Entrez le nom du fichier dans lequel écrire (N'oubliez pas d'inscrire également son extension s'il en possède une!)\n"), "a")
		print("Bien! Vous pouvez désormais commencer à taper votre texte.")
		while True:
			ligne = input()
			if ligne == "":
				break
			else:
				fichier.write(ligne+"\n")
		fichier.close()
		print("Fin de l'éciture! Retour au menu principal!")
		__main__()
	elif answer in ["L","l"]:
		boucle = True
		while boucle:
			try:
				fichier = open(input("Entrez le chemin d'accès vers un fichier valide pour le lire\n"), "r")
				boucle = False
			except:
				print("Fichier invalide! Entrez un chemin d'accès très valide!")
		print("Voici le contenu de votre fichier:")
		content = fichier.read()
		print(content)
		print("Fin du fichier! Retour au menu principal!")
		__main__()

__main__()
