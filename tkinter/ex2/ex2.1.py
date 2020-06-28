"ISN - Python - TKinter - Exercice 2"
"Programme qui affiche un dessin comportant ses carrés, triangles, étoiles à 5 et 6 branches."

#######################################################
# Encodage: UTF-8                                     #
# Programme Python 3.7                                #
# Auteur : Antoine Cheucle                            #
# Pas de liscence, libre d'utilisation                #
# Dépendences: module TKinter                         #
#######################################################

#########################################
#Importation des modules externes:
from tkinter import *

#Corps principal du programme:
def __main__():
    fen = Tk()
    canvas = Canvas(fen, bg="white", height=500, width=500)
    canvas.pack(side=TOP)
    quit_fen = Button(fen, text="Quitter", command = fen.quit)
    quit_fen.pack(side=BOTTOM)

    canvas.create_oval(100,100,200,200,width=8, outline="blue")
    canvas.create_oval(220,100,320,200,width=8, outline="black")
    canvas.create_oval(340,100,440,200,width=8, outline="red")
    canvas.create_oval(160,150,260,250,width=8, outline="yellow")
    canvas.create_oval(280,150,380,250,width=8, outline="green")


    fen.mainloop()
    fen.destroy()


__main__()