import random
import time
from tkinter import *
import monstre
import tour
import projectile


class Vue:
    def __init__(self, parent):
        self.parent = parent

        self.modele = self.parent.modele
        self.root = Tk()
        self.root.title("TowerDefence, alpha_0.1")
        self.creer_interface()

    def creer_interface(self):
        # cadre HUD affichant la duree
        self.bg = PhotoImage(file="Images/carte.png")
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

        self.canevas.create_image(self.modele.largeur_carte / 2, self.modele.hauteur_carte / 2, image=self.bg)
        for i in self.modele.liste_monstres_terrain:
            self.canevas.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, fill="black")
        for i in self.modele.liste_tours:
            self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                          i.y + i.demie_taille, fill="black",
                                          stipple="@Images/Question-Mark-Emoji100x100.xbm", offset="center")


class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.largeur_carte = 1200
        self.hauteur_carte = 800
        self.path = [[200, 450], [200, 200], [440, 200], [440, 520], [760, 520], [760, 370], [1250, 370]]
        self.vague = 0
        self.liste_monstres_terrain = []
        self.liste_monstres_entrepot = []
        self.liste_projectiles = []
        self.liste_tours = []
        self.delai_creation_creep = 0
        self.delai_creation_creep_max = 50
        self.nb_creep_vague = 2

        self.creer_tour()


    def creer_monstre(self):
        for i in range(self.nb_creep_vague * self.vague):
            self.liste_monstres_entrepot.append(monstre.Monstre(-10, 450))

    def creer_tour(self):

        self.liste_tours.append(tour.Tour(320, 290, 200, 50))
        self.liste_tours.append(tour.Tour(535, 425, 200, 50))
        self.liste_tours.append(tour.Tour(645, 425, 200, 50))

    def bouger_monstres(self):

        for i in self.liste_monstres_terrain:
            i.avancer_monstre(self.path)
        self.tuer_monstre()

    def tuer_monstre(self):
        for i in self.liste_monstres_terrain:
            if i.x > 1240:
                self.liste_monstres_terrain.remove(i)

    def jouer_partie(self):
        self.spawn_monstre_terrain()
        self.attaque_tours()
        self.mouvement_projectiles()


    def spawn_monstre_terrain(self):
        self.delai_creation_creep += 1
        if self.delai_creation_creep == self.delai_creation_creep_max and len(self.liste_monstres_entrepot) != 0:
            temp = self.liste_monstres_entrepot.pop(0)
            self.liste_monstres_terrain.append(temp)
            self.delai_creation_creep = 0
        if len(self.liste_monstres_terrain) != 0:
            self.bouger_monstres()
        if len(self.liste_monstres_entrepot) == 0 and len(self.liste_monstres_terrain) == 0:
            self.vague += 1
            self.creer_monstre()
            self.delai_creation_creep = 0
            self.delai_creation_creep_max -= 5


    def attaque_tours(self):
        for tour in self.liste_tours:
            tour.delai_tire += 1
            for monstre in self.liste_monstres_terrain:
                    if tour.analyse_rayon(monstre) and tour.delai_tire >= tour.vitesse_attaque:
                        tour.delai_tire = 0
                        self.liste_projectiles.append(projectile.Projectile(tour,monstre))

    def mouvement_projectiles(self):
        if len(self.liste_projectiles) != 0:
            for projectile in self.liste_projectiles:
                projectile.lancer_projectile()
                if projectile.y == projectile.cibleY and projectile.x == projectile.cibleX:
                     #LE MINION EST TOUCHÉ
                    self.liste_projectiles.remove(projectile) ##watch out



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

    def jouer_partie(self):
        if self.partie_en_cours:
            self.modele.jouer_partie()
            self.vue.root.after(40, self.jouer_partie)
        self.vue.afficher_partie()


if __name__ == '__main__':
    c = Controleur()
    print("L'application se termine")
