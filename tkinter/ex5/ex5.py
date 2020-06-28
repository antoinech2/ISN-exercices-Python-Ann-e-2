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

#Corps principal du programme:

def main():
	global canv
	fen = Tk()
	Label(fen, text = "Premier champ:").grid(row = 0, sticky = E)
	Label(fen, text = "Second:").grid(row = 1, sticky = E)
	Label(fen, text = "Troisième:").grid(row = 2, sticky = E)
	Entry(fen).grid(row = 0,column = 1)
	Entry(fen).grid(row = 1,column = 1)
	Entry(fen).grid(row = 2,column = 1)
	canv = Canvas(fen, width = 160, height = 160)
	photo = PhotoImage(file="chat.gif")
	img = canv.create_image(80,80,image = photo)
	canv.grid(row = 0,column = 3, rowspan=3, padx=10, pady=5)
	fen.mainloop()

main()
