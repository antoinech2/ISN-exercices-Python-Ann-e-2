"ISN - Python - TKinter - Exercice 7"
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

color_pieton = "red"
color_voiture = "green"

def DrawCircle(coords, rayon, coul):
	"Fonction pour tracer un cercle"
	canv.create_oval(coords[0]-rayon, coords[1]-rayon, coords[0]+rayon, coords[1]+rayon, outline="black", fill=coul)

def DrawFeux():
    DrawCircle((475,475),15,color_voiture)
    DrawCircle((175,175),15,color_voiture)
    DrawCircle((475,425),15,color_pieton)
    DrawCircle((175,225),15,color_pieton)

def ChangeColor():
    global color_pieton,color_voiture
    if color_pieton == "red":
        color_pieton = "green"
        color_voiture = "red"
    else:
        color_pieton = "red"
        color_voiture = "green"
    DrawFeux()


#Corps principal du programme:
def __main__():
    global canv
    fen = Tk()
    canv = Canvas(fen, width = 600, height = 600)
    canv.pack(side=TOP, pady=5)
    button = Button(fen, text="Basculer les feux", command=ChangeColor)
    button.pack(side=BOTTOM)

    canv.create_rectangle(200,2,450,599, fill="darkgray")
    canv.create_rectangle(200,200,250,450, fill="yellow")
    canv.create_rectangle(300,200,350,450, fill="yellow")
    canv.create_rectangle(400,200,450,450, fill="yellow")
    DrawFeux()

    fen.mainloop()

__main__()