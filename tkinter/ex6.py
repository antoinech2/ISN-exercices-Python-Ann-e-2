"ISN - Python - TKinter - Exercice 6"
"Description."

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
from math import sqrt

#Corps principal du programme:
pos = [(300,500),(500,500)]
rayon = [100,60]
deplacement = 30

def DrawCircle(coords, rayon, coul):
	"Fonction pour tracer un cercle"
	cercle = canv.create_oval(coords[0]-rayon, coords[1]-rayon, coords[0]+rayon, coords[1]+rayon, outline=coul)
	return cercle

def Move(cercle_id, direction):
	global canv, cercle, pos, distance_lab
	(x,y) = pos[cercle_id]
	if direction == "right":
		pos[cercle_id] = (x+deplacement,y)
	elif direction == "left":
		pos[cercle_id] = (x-deplacement,y)
	elif direction == "top":
		pos[cercle_id] = (x,y-deplacement)
	elif direction == "bottom":
		pos[cercle_id] = (x,y+deplacement)
	(x,y) = pos[cercle_id]
	canv.coords(cercle[cercle_id], x-rayon[cercle_id], y-rayon[cercle_id], x+rayon[cercle_id], y+rayon[cercle_id])
	distance = sqrt((pos[0][0]-pos[1][0])**2+(pos[0][1]-pos[1][1])**2)
	distance_lab.configure(text= "Distance : {0:.2f}".format(distance))

def MoveLeft0():
	Move(0,"left")

def MoveRight0():
	Move(0,"right")

def MoveUp0():
	Move(0,"top")

def MoveDown0():
	Move(0,"bottom")

def MoveLeft1():
	Move(1,"left")

def MoveRight1():
	Move(1,"right")

def MoveUp1():
	Move(1,"top")

def MoveDown1():
	Move(1,"bottom")


def __main__():
	global canv, cercle, distance_lab
	fen = Tk()
	canv = Canvas(fen, width = 600, height = 600)
	canv.grid(row = 0, column = 0, columnspan = 7)
	cercle = [DrawCircle(pos[0],rayon[0],"blue")],[DrawCircle(pos[1],rayon[1],"red")]
	Button(fen, text="Gauche", fg="blue", command = MoveLeft0).grid(row = 3, column = 0, sticky=E)
	Button(fen, text="Haut", fg="blue", command = MoveUp0).grid(row = 2, column = 1)
	Button(fen, text="Droite", fg="blue", command = MoveRight0).grid(row = 3, column = 2, sticky=W)
	Button(fen, text="Bas", fg="blue", command = MoveDown0).grid(row = 4, column = 1)

	Button(fen, text="Gauche", fg="red", command = MoveLeft1).grid(row = 3, column = 4, sticky=E)
	Button(fen, text="Haut", fg="red", command = MoveUp1).grid(row = 2, column = 5)
	Button(fen, text="Droite", fg="red", command = MoveRight1).grid(row = 3, column = 6, sticky=W)
	Button(fen, text="Bas", fg="red", command = MoveDown1).grid(row = 4, column = 5)

	distance_lab = Label(fen, text="Distance")
	distance_lab.grid(row = 1, column = 0, columnspan = 7)
	fen.mainloop()

__main__()
