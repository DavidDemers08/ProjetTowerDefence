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

    def creer_tour(self, event):

        self.parent.creer_tour(event)

    def creer_interface(self):
        # cadre HUD affichant la duree
        self.bg = PhotoImage(file="Images/carte.png")
        self.bg.width()

        self.cadre_depart = Frame(self.root, bg='gray')
        bouton_depart = Button(self.cadre_depart, text='Commencer la partie', command=self.parent.debuter_partie)

        self.image_vie = PhotoImage(file="Images/health_bar.png")
        label_image_vie = Label(self.cadre_depart, image=self.image_vie, height=17, width=96)

        self.image_argent = PhotoImage(file="Images/money.png")
        label_image_argent = Label(self.cadre_depart, image=self.image_argent, height=17)

        #self.var_argent = StringVar()
        label_argent = Label(self.cadre_depart, text='0,00$', width=10)  #textvariable=self.var_argent

        self.canevas = Canvas(self.root, width=self.modele.largeur_carte, height=self.modele.hauteur_carte)

        self.cadre_depart.pack(expand=True, fill=BOTH)
        bouton_depart.pack(side=LEFT)
        label_argent.pack(side=RIGHT)
        label_image_argent.pack(side=RIGHT)
        label_image_vie.pack(side=RIGHT, padx=20)
        self.canevas.pack()

        self.afficher_partie()
        for i in self.modele.liste_tours:
            self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                          i.y + i.demie_taille, fill="black", stipple="gray25")

    def afficher_partie(self):
        self.canevas.delete(ALL)

        demitaille = 50

        self.canevas.create_image(self.modele.largeur_carte / 2, self.modele.hauteur_carte / 2, image=self.bg,
                                  tags="bg")
        self.canevas.tag_bind("bg", "<Button-1>", self.creer_tour)

        self.canevas.create_rectangle(0, 400, 240, 475, fill="", outline="")
        self.canevas.create_rectangle(160, 160, 240, 400, fill="", outline="")
        self.canevas.create_rectangle(160, 160, 485, 250, fill="", outline="")
        self.canevas.create_rectangle(400, 160, 485, 560, fill="", outline="")
        self.canevas.create_rectangle(400, 480, 800, 560, fill="", outline="")
        self.canevas.create_rectangle(720, 320, 800, 560, fill="", outline="")
        self.canevas.create_rectangle(720, 320, 1200, 400, fill="", outline="")

        for i in self.modele.liste_monstres_terrain:
            self.canevas.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, fill="black", tags='monstre')
            x1 = i.x - 10
            x2 = x1 + 20
            x3 = x1 + (i.vie / monstre.Monstre.vie_max * 20)
            self.canevas.create_rectangle(x1, i.y - 15, x2, i.y - 10, fill="red")
            self.canevas.create_rectangle(x1, i.y - 15, x3, i.y - 10, fill="green")

        for i in self.modele.liste_tours:
            self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                          i.y + i.demie_taille, fill="red")
            self.canevas.create_oval(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                     i.y + i.demie_taille, fill="black")

            self.canevas.create_oval(i.x - i.rayon, i.y - i.rayon, i.x + i.rayon, i.y + i.rayon, fill="")

            if len(i.liste_projectiles) != 0:
                for projectile in i.liste_projectiles:
                    self.canevas.create_oval(projectile.x - 5, projectile.y - 5, projectile.x + 5, projectile.y + 5,
                                             fill="blue")

    def afficher_fin_partie(self):
        print("fin de partie")



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
        self.delai_creation_creep_max = 10
        self.nb_creep_vague = 5
        self.pointage = 0
        self.vie = 3

    def creer_monstre(self):
        if len(self.liste_monstres_entrepot) == 0 and len(self.liste_monstres_terrain) == 0:
            self.vague += 1
            for i in range(self.nb_creep_vague * self.vague):
                self.liste_monstres_entrepot.append(monstre.Monstre(-10, 450))
            self.delai_creation_creep = 0



    def bouger_monstres(self):
        if len(self.liste_monstres_terrain) != 0:
            for i in self.liste_monstres_terrain:
                i.avancer_monstre(self.path)

    def jouer_partie(self):
        self.creer_monstre()
        self.spawn_monstre()
        self.bouger_monstres()
        self.attaque_monstres()
        self.verifier_etat_monstre()
        self.verifier_etat_joueur()
        print(self.vie)

    def spawn_monstre(self):
        self.delai_creation_creep += 1
        if self.delai_creation_creep == self.delai_creation_creep_max and len(self.liste_monstres_entrepot) != 0:
            temp = self.liste_monstres_entrepot.pop(0)
            self.liste_monstres_terrain.append(temp)
            self.delai_creation_creep = 0


    def attaque_monstres(self):
        for tour in self.liste_tours:
            tour.attaque(self.liste_monstres_terrain)

    def creer_tours(self, event):
        x = event.x
        y = event.y
        self.liste_tours.append(tour.Tour(x, y, 200, 10))

    def verifier_etat_monstre(self):
        for i in self.liste_monstres_terrain:
            if i.vie <= 0:
                self.pointage += 5
                self.liste_monstres_terrain.remove(i)
            if i.x > 1240:
                self.liste_monstres_terrain.remove(i)
                if self.vie > 0:
                    self.vie -= 1

    def verifier_etat_joueur(self):
        if self.vie == 0:
            self.parent.partie_en_cours = 0

    def reinitialiser(self):
        self.liste_monstres_terrain = []
        self.liste_monstres_entrepot = []
        self.liste_projectiles = []
        self.liste_tours = []
        self.vie = 3
        self.vague = 0
        self.creer_monstre()

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
            self.modele.vague += 1

    def jouer_partie(self):
        if self.partie_en_cours:
            self.modele.jouer_partie()
            self.vue.root.after(40, self.jouer_partie)
        else:
            self.finir_partie()
        self.vue.afficher_partie()

    def finir_partie(self):
        self.vue.afficher_fin_partie()
        self.modele.reinitialiser()


    def creer_tour(self, event):
        if self.partie_en_cours == 1:
            self.modele.creer_tours(event)


if __name__ == '__main__':
    c = Controleur()
    print("L'application se termine")
