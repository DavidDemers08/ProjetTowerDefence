import random
from tkinter import *


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

    def afficher_partie(self):
        self.canevas.delete(ALL)

        self.canevas.create_rectangle(0, self.modele.hauteur_carte / 2 - 50, self.modele.largeur_carte,
                                      self.modele.hauteur_carte / 2 + 50, fill="beige")

        self.canevas.create_image(self.modele.largeur_carte/2, self.modele.hauteur_carte/2, image=self.bg)
        for i in self.modele.liste_monstres:
            self.canevas.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, fill="black")


class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.largeur_carte = 1200
        self.hauteur_carte = 800
        self.vague = 0
        self.liste_monstres = []

    def creer_monstre(self):

        for i in range(50):
            self.liste_monstres.append(Monstre(-10, random.randrange(350, 450)))

    def bouger_monstres(self):

        for i in self.liste_monstres:
            i.avancer_monstre()


class Monstre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 3

    def avancer_monstre(self):
        self.x += self.vitesse


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
