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
from random import randint, randrange, random
from math import sqrt

ball_speed=0.2
vitesse = (0.1,0.1)
coordonnee = (300, 300)
fenetre = (600,600)

def DrawCircle(coords, rayon, coul):
	"Fonction pour tracer un cercle"
	ball = canv.create_oval(coords[0]-rayon, coords[1]-rayon, coords[0]+rayon, coords[1]+rayon, outline="black", fill=coul)
	return ball

def ChangeDirection():
    global vitesse
    y = random()*ball_speed

    x = sqrt(ball_speed**2+y**2)
    y = sqrt(ball_speed**2+x**2)
    print(x, y)
    vitesse = (x ,y)

def MoveBall():
    global coordonnee,vitesse
    rand = randint(0,20)
    if rand == 0:
        ChangeDirection()
    coordonnee = (coordonnee[0]+vitesse[0], coordonnee[1]+vitesse[1])
    canv.coords(balle, coordonnee[0]-20, coordonnee[1]-20, coordonnee[0]+20, coordonnee[1]+20)
    if (coordonnee[0] < 0) or (coordonnee[0] > fenetre[0]):
        vitesse = (-vitesse[0] ,vitesse[1])
    if (coordonnee[1] < 0) or (coordonnee[1] > fenetre[1]):
        vitesse = (vitesse[0] ,-vitesse[1])

    if game_running:
        fen.after(10, MoveBall)

def StartGame():
    global game_running, balle
    balle = DrawCircle(coordonnee, 20, "red")
    game_running = True
    MoveBall()


def StopGame():
    global game_running
    game_running = False
    fen.quit()
    fen.destroy()

def __main__():
    global canv, fen
    fen = Tk()
    canv = Canvas(fen, width=fenetre[0], height = fenetre[1])
    canv.pack(side=TOP)
    but_start = Button(fen, text="Démarrer le jeu", command=StartGame)
    but_start.pack(side=BOTTOM)
    but_stop = Button(fen, text="Arrêter le jeu", command=StopGame)
    but_stop.pack(side=BOTTOM)

    fen.mainloop()

__main__()