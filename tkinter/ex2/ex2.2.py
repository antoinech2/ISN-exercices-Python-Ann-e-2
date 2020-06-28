"ISN - Python - TKinter - Exercice 2"
"Programme qui affiche un dessin comportant ses carrés, triangles, étoiles à 5 et 6 branches."

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

#Définition des fonctions:

def DrawCircle(id):
    if id == "bleu":
        canv.create_oval(100,100,200,200,width=8, outline="blue")
    elif id == "rouge":
        canv.create_oval(340,100,440,200,width=8, outline="red")
    elif id == "noir":
        canv.create_oval(220,100,320,200,width=8, outline="black")
    elif id == "jaune":
        canv.create_oval(160,150,260,250,width=8, outline="yellow")
    elif id == "vert":
        canv.create_oval(280,150,380,250,width=8, outline="green")

#TODO: Faire une fonction cercle pour tracer un cercle avec oval

#Corps principal du programme:

def __main__():
    fen = Tk()
    canv = Canvas(fen, bg="white", height=500, width=500)
    canv.pack(side=TOP)
    quit_fen = Button(fen, text="Quitter", command = fen.quit)
    quit_fen.pack(side=BOTTOM)

    bouton_circle_red = Button(fen, text="Afficher l'anneau rouge", command = DrawCircle("rouge"))
    bouton_circle_red.pack(side=RIGHT)

    fen.mainloop()
    fen.destroy()
__main__()
