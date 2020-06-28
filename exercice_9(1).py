"ISN - Python - Partie 1 - Exercice 9"
"Programme qui affiche le nom des mois avec leur nombre de jours."

#Liste des jours dans chaque mois
jours=[31,28,31,30,31,30,31,31,30,31,30,31]

#Liste des noms des mois
mois=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

#Troisième liste qui va contenir les éléments des deux premières
nbjour=[]

#Boucle 12 fois pour chaque éléments des listes "jours" et "mois".
for nb in range (12):
    nbjour.append(mois[nb])
    nbjour.append(jours[nb])


#Boucle 12 fois pour afficher les mois et les jours.
for nb in range (12):
    print(nbjour[nb*2],":",nbjour[nb*2+1], sep='')
