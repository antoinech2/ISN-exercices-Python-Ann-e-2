#ISN - Python - Partie 1 - Exercice complémentaire 2
#Programme qui indique si un triangle est rectangle en fontion de ces 3 côtés

longeur = []
longeur_name = ["AB", "BC", "AC"]
longeur_valide = [False, False, False]

print("Soit ABC un triangle")

#On stocke les valeurs des longeurs des trois côtés en vérifiant qu'il soient bien des nombres
for loop in range (3):
    while longeur_valide[loop] == False:
        try:
            imput=float(input("Entrer la longeur du côté "+str(longeur_name[loop]+" : ")))
        except ValueError:
            print("Erreur: Merci d'entrer un nombre valide!")
        else:
            if imput<=0:
                print("Erreur: Merci d'entrer une longeur positive!")
            else:
                longeur_valide[loop] = True
    longeur.append(imput)

#On cherche la plus grande valeur
max = 0
for loop in range (3):
    if longeur[loop] > max:
        max = longeur[loop]
        max_index = loop
print("Le côté le plug grand est",longeur_name[max_index])

#On applique pythagore
cotes = 0
for loop in range (3):
    if not loop == max_index:
        cotes += longeur[loop]**2
if max**2 == cotes:
    print("Le trigangle est rectangle!")
else:
    print("Le triangle n'est pas rectangle!")
