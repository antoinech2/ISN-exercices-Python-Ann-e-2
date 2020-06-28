"ISN - Python - Partie 2 - Exercice 4"
"Programme qui demande une année et indique si elle est bissextile ou pas"

# Coding: UTF-8

#Programme Python 3.2
#Auteur : Antoine Cheucle
#Pas de liscence
valide=False
while valide == False:
    annee=input("Entrée une année (nombre entier")
    try:
        annee = int(annee)
        valide = True
    except ValueError:
        print("Erreur: Nombre invalide. Entrez un nombre entier")

if (annee%4) or (not annee%100 and annee%400):
    print("L'année",annee,"n'est pas une année bissextile.")
else:
    print("L'année",annee,"est une année bissextile.")