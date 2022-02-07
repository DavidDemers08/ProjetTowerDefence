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
        self.cadre_info.pack()
        self.afficher_partie()
        self.cadre_info.create_rectangle(0, self.modele.hauteur / 2 - 50, self.modele.largeur,
                                         self.modele.hauteur / 2 + 50, fill="beige")

    def afficher_partie(self):
        pass



class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 1000
        self.hauteur = 800
        self.chemin = [[self.largeur,self.hauteur/2]] #tableau de chemin (ici juste la ligne droite)
        self.monstreList = []
        self.creer_monstres()


    def avancer_monstres(self):
        pass

    def creer_monstres(self):
        for i in range(51):
            self.monstreList.append(Monstre(-10,random.randrange(350,450)))



class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.root.mainloop()
        self.modele.creer_monstres()


if __name__ == '__main__':
    c = Controleur()
    print("Fin du programme")
