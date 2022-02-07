import random
from tkinter import *

from monstre import Monstre


class Vue:
    def __init__(self, parent):
        self.parent = parent
        self.modele = self.parent.modele
        self.root = Tk()
        self.root.title("TowerDefence 0.1")
        self.creer_interface()

    def creer_interface(self):
        self.cadre_info = Canvas(self.root, bg="darkgreen", height=self.modele.hauteur,
                                 width=self.modele.largeur)
        self.cadre_info.create_rectangle(0, self.modele.hauteur / 2 - 50, self.modele.largeur,
                                         self.modele.hauteur / 2 + 50, fill="beige")
        self.cadre_info.pack()
        self.afficher_partie()

    def afficher_partie(self):
        for i in self.modele.monstreList:
            self.cadre_info.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, fill="red")


class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 1000
        self.hauteur = 800
        self.chemin = [(self.largeur, self.hauteur / 2)]  # tableau de chemin (ici juste la ligne droite)
        self.monstreList = []
        self.creer_monstres()

    def avancer_monstres(self):
        for i in self.monstreList:
            i.avancer_monstre(1000, 400)

    def creer_monstres(self):
        for i in range(51):
            self.monstreList.append(Monstre(-10, random.randrange(350, 450)))


class Controleur:
    def __init__(self):
        self.partie_en_cours = 0
        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.root.mainloop()

    def debuter_partie(self):
        self.partie_en_cours = 1
        self.modele.creer_monstres()
        self.jouer_partie()

    def jouer_partie(self):
        if self.partie_en_cours:
            self.vue.root.after(40, self.jouer_partie)
        self.vue.afficher_partie()


if __name__ == '__main__':
    c = Controleur()
    print("Fin du programme")
