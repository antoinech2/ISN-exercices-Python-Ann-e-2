"ISN - Python - Partie 1 - Exercice 9"
"Programme qui affiche le nom des mois avec leur nombre de jours sur la même ligne."

#Liste des jours dans chaque mois
jours=[31,28,31,30,31,30,31,31,30,31,30,31]

#Liste des noms des mois
mois=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

#Troisième liste qui va contenir les éléments des deux premières
mois_jours=[]

#On ajoute chaque élément des listes "jours" et "mois" dans la nouvelle liste alternativement.
for nb in range (12):
    mois_jours.append(mois[nb])
    mois_jours.append(jours[nb])


#On boucle 12 fois pour afficher les mois et le nombre de jours associés.
for nb in range (12):
    #Le nom du mois correspond à l'index nb*2, on ajoute 1 pour avoir le nombre de jours
    print(mois_jours[nb*2],":",mois_jours[nb*2+1], sep='')
