import random
from tkinter import *

from monstre import Monstre


class Vue:
    def __init__(self, parent):
        self.parent = parent

        self.modele = self.parent.modele
        self.root = Tk()
        self.root.title("TowerDefence, alpha_0.1")
        self.creer_interface()

    def creer_interface(self):
        # cadre HUD affichant la duree
        self.bg = PhotoImage(file="carte.png")
        self.bg.width()

        cadre_depart = Frame(self.root, bg='gray')
        bouton_depart = Button(cadre_depart, text='Commencer la partie', command=self.parent.debuter_partie)
        self.canevas = Canvas(self.root, width=self.modele.largeur_carte, height=self.modele.hauteur_carte)

        cadre_depart.pack(expand=True, fill=BOTH)
        bouton_depart.pack(side=TOP)

        self.canevas.pack()

        self.afficher_partie()
        for i in self.modele.liste_tours:
            self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                          i.y + i.demie_taille, fill="black", stipple="gray25")
    def afficher_partie(self):
        self.canevas.delete(ALL)

        self.canevas.create_rectangle(0, self.modele.hauteur_carte / 2 - 50, self.modele.largeur_carte,
                                      self.modele.hauteur_carte / 2 + 50, fill="beige")

        self.canevas.create_image(self.modele.largeur_carte/2, self.modele.hauteur_carte/2, image=self.bg)
        for i in self.modele.liste_monstres:
            self.canevas.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, fill="black")
        for i in self.modele.liste_tours:
            self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                          i.y + i.demie_taille, fill="black", stipple="gray25")


class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.largeur_carte = 1200
        self.hauteur_carte = 800
        self.vague = 0
        self.liste_monstres = []
        self.liste_tours = []
        self.creer_tour()

    def creer_monstre(self):

        for i in range(50):
            self.liste_monstres.append(Monstre(-10, random.randrange(350, 450)))

    def creer_tour(self):

        self.liste_tours.append(Tour(300,400,5,50))


    def bouger_monstres(self):

        for i in self.liste_monstres:
            i.avancer_monstre(0,350)

class Tour:
    def __init__(self, x, y, rayon,demie_taille):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.demie_taille = demie_taille

    def emplacement_valide(self):
        pass



class Controleur:
    def __init__(self):
        self.partie_en_cours = 0

        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.root.mainloop()

    def debuter_partie(self):
        if not self.partie_en_cours:
            self.partie_en_cours = 1
            self.jouer_partie()
            self.modele.vague = 1
            self.modele.creer_monstre()


    def jouer_partie(self):
        if self.partie_en_cours:
            self.vue.root.after(40, self.jouer_partie)
            self.modele.bouger_monstres()
        self.vue.afficher_partie()


if __name__ == '__main__':
    c = Controleur()
    print("L'application se termine")
