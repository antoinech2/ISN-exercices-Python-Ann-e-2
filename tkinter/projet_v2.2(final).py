"ISN - Python - TKinter - Mini-projet"
"Jeu du clic-balle"
"Une balle se déplace au hasard sur un canevas, à vitesse faible.\
Le joueur doit essayer de cliquer sur cette balle à l'aide de la souris.\
S'il y arrive, il gagne un point, mais la balle se\
déplace plus rapidement et ainsi de suite.\
Arrêter le jeu au bout d'un certain nombre de clics et afficher le score atteint."

#######################################################
# Encodage: UTF-8                                     #
# Programme Python 3.7                                #
# Auteurs : Antoine Cheucle  et   Titouan Escaille    #
# Pas de licence, libre d'utilisation                 #
# Dépendences: module TKinter, random, math           #
#######################################################

#########################################
#Importation des modules externes:
from tkinter import *
from random import randint, random
from math import sqrt, pi, cos, sin
from tkinter.messagebox import showinfo
#########################################

#########################################
#Définition des constantes de jeu:
fenetre = (800,600)              # Taille de la fenêtre (x,y) (canvas)
ball_size = 20                   # Rayon de la balle
change_direction_chance = 100    # Chance de changement de direction
#Définition des variables de jeu:
ball_speed = 0.8                 # Vitesse initiale de la balle
ball_position = [300, 300]       # Coordonnées initiales de la balle [x,y]
game_running = False             # Etat du jeu initial
points = 0                       # Nombre de points du joueur
clics_restants = 30              # Nombre maximun de clics autorisés
#########################################

def __main__():
    "Programme principal, création de la fenêtre graphique"
    global canv, fen, text_points
    #Création de la fenêtre graphique
    fen = Tk()
    canv = Canvas(fen, width=fenetre[0], height = fenetre[1])
    canv.pack(side=TOP)
    #Liaison du clic de souris avec le canvas
    canv.bind("<Button-1>", Clic)
    but_stop = Button(fen, text="Quitter le jeu", command=StopGame)
    but_stop.pack(side=BOTTOM)
    but_start = Button(fen, text="Démarrer le jeu", command=StartGame)
    but_start.pack(side=BOTTOM)
    text_points = Label(fen, text = "Cliquez sur 'Démarrer le jeu' pour commencer!")
    text_points.pack(side=BOTTOM)

    #Démarrage du réceptionnaire d'évènements
    fen.mainloop()

#Définition des fonctions des gestionnaires d'évènements:

def StartGame():
    "Démarrage du jeu"
    global game_running, ball
    if game_running == False:
        #Création de la balle
        ball = canv.create_oval(ball_position[0]-ball_size, ball_position[1]-ball_size,\
                ball_position[0]+ball_size, ball_position[1]+ball_size, outline="black", fill="red")
        #Démarrage du jeu
        game_running = True
        #Définition d'une direction initiale
        ChangeDirection()
        #Démarrage du mouvement de la balle
        MoveBall()
        text_points.configure(text= "Essayez de cliquer sur la balle un maximum de fois!")

def StopGame():
    "Arrêt du jeu"
    global game_running
    #Arrêt de la boucle principale
    game_running = False
    #Fermeture de la fenêtre
    fen.quit()
    fen.destroy()

def MoveBall():
    "Procédure générale de déplacement"
    global ball_position,vitesse

    #Générateur RNG pour choisir si on doit changer la direction
    if randint(0,change_direction_chance) == 0:
        ChangeDirection()

    #Calcul de la nouvelle possition en appliquant la vitesse à la position pour déplacer la balle en fonction de sa direction
    ball_position = [ball_position[0]+vitesse[0], ball_position[1]+vitesse[1]]

    #Vérification que la balle ne soit pas sortie du canvas, et changement de position et direction si c'est le cas
    #Gauche
    if ball_position[0]-ball_size < 0:
        vitesse[0] = -vitesse[0]
        ball_position[0] = ball_size
    #Droite
    elif ball_position[0]+ball_size > fenetre[0]:
        vitesse[0] = -vitesse[0]
        ball_position[0] = fenetre[0]-ball_size
    #Haut
    if ball_position[1]-ball_size < 0:
        vitesse[1] = -vitesse[1]
        ball_position[1] = ball_size
    #Bas
    elif ball_position[1]+ball_size > fenetre[1]:
        vitesse[1] = -vitesse[1]
        ball_position[1] = fenetre[1]-ball_size

    #Mise à jour de la position graphique de la balle
    canv.coords(ball, ball_position[0]-ball_size, ball_position[1]-ball_size, ball_position[0]+ball_size, ball_position[1]+ball_size)

    #Appel de la fonction récursivement après un délai si le jeu n'est pas arrêté.
    if game_running:
        fen.after(10, MoveBall)

def ChangeDirection():
    "Procédure générale de changement de direction"
    global vitesse

    #Calcul d'un angle aléatoire (entre 0 et 2pi rad)
    new_angle = random()*2*pi

    #Calcul des composantes x et y de la vitesse en fonction de l'angle
    vitesse_x = cos(new_angle)*ball_speed
    vitesse_y = sin(new_angle)*ball_speed

    #Définition de la nouvelle vitesse avec le nouvel angle
    vitesse = [vitesse_x ,vitesse_y]

def Clic(event):
    "Procédure de traitement du clic de souris sur le canvas"
    global points, ball_speed, clics_restants, game_running
    if game_running:
        clics_restants -= 1
        # On vérifie si le clic est dans la balle
        if (event.x <= ball_position[0] + ball_size and event.x >= ball_position[0] - ball_size)\
        and (event.y <= ball_position[1] + ball_size and event.y >= ball_position[1] - ball_size):
            #On augmente les points et la vitesse
            points += 1
            ball_speed += 0.4
            ChangeDirection()
        #On rafraîchit le texte du label
        text_points.configure(text= "Nombre de points : " + str(points) + "\nNombre de clics restants : " + str(clics_restants))
        if clics_restants == 0 :
            #On arrête le jeu si le nombre de clic est épuisé
            game_running = False
            #On affiche une infobulle pour afficher le score final.
            showinfo("info","Le jeu est terminé !! \nVous avez " + str(points) + " points!")
            StopGame()

#Appel de la fonction principale
__main__()
