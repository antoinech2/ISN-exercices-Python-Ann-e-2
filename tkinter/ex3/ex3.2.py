"ISN - Python - TKinter - Exercice 3"
"Programme qui affiche un damier noir et blanc."

#######################################################
# Encodage: UTF-8                                     #
# Programme Python 3.7                                #
# Auteur : Antoine Cheucle                            #
# Pas de licence, libre d'utilisation                 #
# Dépendences: module TKinter                         #
#######################################################

#########################################
#Importation des modules externes:
from tkinter import *
from random import randint

#Fonctions:

def ShowDamier():
	"Affiche le damier"
	canv.delete(ALL)
	for ligne in range (10):
		for colonne in range (5):
			canv.create_rectangle(2*colonne*60+(ligne%2)*60,ligne*60,2*colonne*60+60+(ligne%2)*60,ligne*60+60, fill="black")

def DrawCircle(coords, rayon, coul):
	"Fonction pour tracer un cercle"
	canv.create_oval(coords[0]-rayon, coords[1]-rayon, coords[0]+rayon, coords[1]+rayon, outline=coul, fill=coul)

def ShowPion():
	taille = 20
	colonne = randint(0,9)
	ligne = randint(0,9)
	DrawCircle((colonne*60+30,ligne*60+30), taille, "red")

#Corps principal du programme:

def main():
	global canv
	fen = Tk()
	canv = Canvas(fen, width=600, height=600)
	canv.pack(side=TOP, pady=10, padx=10)
	button_show = Button(fen, text = "Afficher le damier", command = ShowDamier)
	button_show.pack(side=LEFT, padx=6, pady=6)
	button_quit = Button(fen, text = "Quitter", command = fen.quit)
	button_quit.pack(side=RIGHT, padx=6, pady=6)
	button_pion = Button(fen, text = "Afficher un pion", command = ShowPion)
	button_pion.pack(side=BOTTOM, padx=6, pady=6)
	fen.mainloop()

main()
