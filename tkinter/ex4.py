# Détection et positionnement d'un clic de souris dans une fenêtre :

from tkinter import *

def DrawCircle(coords, rayon, coul):
	"Fonction pour tracer un cercle"
	cadre.create_oval(coords[0]-rayon, coords[1]-rayon, coords[0]+rayon, coords[1]+rayon, outline=coul)

def pointeur(event):
        chaine.configure(text = "Clic détecté en X =" + str(event.x) +", Y =" + str(event.y))
        DrawCircle((event.x,event.y),3,"red")

fen = Tk()
cadre = Canvas(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()

fen.mainloop()
