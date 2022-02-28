from tkinter import *

import monstre
import tour
from animer_gif import Animer_gif


class Vue:
    def __init__(self, parent):
        self.parent = parent

        self.modele = self.parent.modele
        self.root = Tk()
        self.root.title("TowerDefence, alpha_0.1")
        self.creer_interface()

    def creer_tour(self, event):
        self.parent.creer_tour(event)

    def creer_tour_glace(self):
        if (self.modele.argent - tour.Tour_Glace.prix) >= 0:
            self.parent.creer_tour_glace()

    def creer_tour_poison(self):
        if (self.modele.argent - tour.Tour_Poison.prix) >= 0:
            self.parent.creer_tour_poison()

    def creer_tour_sniper(self):
        if (self.modele.argent - tour.Tour_Sniper.prix) >= 0:
            self.parent.creer_tour_sniper()

    def creer_interface(self):
        # cadre HUD affichant la duree
        self.canevas = Canvas(self.root, width=self.modele.largeur_carte, height=self.modele.hauteur_carte)
        self.bg = PhotoImage(file="Images/carte.png")
        self.bg.width()

        self.var_vie = StringVar()
        self.var_score = StringVar()
        self.var_vague = StringVar()
        self.var_argent = StringVar()

        self.image_argent = PhotoImage(file="Images/money.png")

        self.cadre_depart = Frame(self.root, bg='gray')

        bouton_depart = Button(self.cadre_depart, text='Commencer la partie', command=self.parent.debuter_partie)
        bouton_tour_glace = Button(self.cadre_depart, text='TOUR GLACE', width=15, height=1, font=('Arial', 6),
                                   command=self.creer_tour_glace)
        bouton_tour_poison = Button(self.cadre_depart, text='TOUR POISON', font=('Arial', 6), width=15, height=1,
                                    command=self.creer_tour_poison)
        bouton_tour_sniper = Button(self.cadre_depart, text='TOUR SNIPER', font=('Arial', 6), width=10, height=1,
                                    command=self.creer_tour_sniper)

        self.canevas.tag_bind("bg", "<Button-1>", self.creer_tour)

        label_image_argent = Label(self.cadre_depart, image=self.image_argent, height=30)
        label_argent = Label(self.cadre_depart, width=10, height=2, font=('Arial', 11),
                             textvariable=self.var_argent)
        label_image_score = Label(self.cadre_depart, text='SCORE', height=1)
        label_vague_texte = Label(self.cadre_depart, text='VAGUE', height=1)
        label_vague = Label(self.cadre_depart, width=5, height=1, font=('Arial', 11),
                            textvariable=self.var_vague)
        label_vie_texte = Label(self.cadre_depart, text='VIE', height=1)
        label_score = Label(self.cadre_depart, width=5, height=1, font=('Arial', 11),
                            textvariable=self.var_vie)
        label_vie = Label(self.cadre_depart, width=5, height=1, font=('Arial', 11),
                          textvariable=self.var_score)

        self.cadre_depart.pack(expand=True, fill=BOTH)
        bouton_depart.pack(side=LEFT, padx=20)
        bouton_tour_glace.pack(side=LEFT, padx=5)
        bouton_tour_poison.pack(side=LEFT, padx=5)
        bouton_tour_sniper.pack(side=LEFT, padx=5)
        label_argent.pack(side=RIGHT)
        label_image_argent.pack(side=RIGHT)
        label_score.pack(side=RIGHT, padx=20)
        label_vie_texte.pack(side=RIGHT, padx=20)
        label_vie.pack(side=RIGHT, padx=20)
        label_image_score.pack(side=RIGHT)
        label_vague.pack(side=RIGHT, padx=20)
        label_vague_texte.pack(side=RIGHT, padx=20)
        self.canevas.pack()

    def afficher_debut_partie(self):
        self.canevas.delete("dynamique")

        self.canevas.create_image(self.modele.largeur_carte / 2, self.modele.hauteur_carte / 2, image=self.bg,
                                  tags=("statique", "bg"))
        self.ouvrir_gif()

    def afficher_partie(self):
        self.canevas.delete("dynamique")
        self.var_argent.set(str(self.modele.argent) + "$")
        self.var_score.set(self.modele.pointage)
        self.var_vie.set(self.modele.vie)
        self.var_vague.set(self.modele.vague)

        self.canevas.tag_bind("bg", "<Button-1>", self.creer_tour)

        self.afficher_path()

        self.afficher_tours()
        for i in self.modele.animations:
            i = self.modele.animations[i]
            self.canevas.create_image(i.x, i.y, image=i.images[i.indice], tags="dynamique")
        self.afficher_monstres()

    def ouvrir_gif(self):
        rep = self.charger_gifs()
        if rep:
            self.parent.creer_anim(rep)

    def charger_gifs(self):
        nom_gif = "Images/portal.gif"
        if nom_gif:
            listeimages = []
            testverite = 1
            noindex = 0
            while testverite:
                try:
                    img = PhotoImage(file=nom_gif, format="gif -index " + str(noindex))
                    listeimages.append(img)
                    noindex += 1
                except Exception:
                    testverite = 0
            return [nom_gif, listeimages]

    def afficher_path(self):
        self.canevas.create_rectangle(0, 400, 240, 475, fill="", outline="", tags="statique")
        self.canevas.create_rectangle(160, 160, 240, 400, fill="", outline="", tags="statique")
        self.canevas.create_rectangle(160, 160, 485, 250, fill="", outline="", tags="statique")
        self.canevas.create_rectangle(400, 160, 485, 560, fill="", outline="", tags="statique")
        self.canevas.create_rectangle(400, 480, 800, 560, fill="", outline="", tags="statique")
        self.canevas.create_rectangle(720, 320, 800, 560, fill="", outline="", tags="statique")
        self.canevas.create_rectangle(720, 320, 1200, 400, fill="", outline="", tags="statique")

    def afficher_monstres(self):
        for i in self.modele.liste_monstres_terrain:

            if isinstance(i, monstre.Monstre):
                self.canevas.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, fill="black", tags=("dynamique"))
                x1 = i.x - 10
                x2 = x1 + 20
                x3 = x1 + (i.vie / monstre.Monstre.vie_max * 20)

                self.canevas.create_rectangle(x1, i.y - 15, x2, i.y - 10, fill="red", tags=("dynamique"))
                self.canevas.create_rectangle(x1, i.y - 15, x3, i.y - 10, fill="green", tags=("dynamique"))

                if i.empoisonne:
                    self.canevas.create_rectangle(x1, i.y - 15, x2, i.y - 10, fill="purple", tags=("dynamique"))
                    self.canevas.create_rectangle(x1, i.y - 15, x3, i.y - 10, fill="green", tags=("dynamique"))
                if i.frozen:
                    #self.canevas.create_rectangle(x1, i.y - 15, x2, i.y - 10, fill="blue", tags=("dynamique"))
                    self.canevas.create_rectangle(x1, i.y - 15, x3, i.y - 10, fill="blue", tags=("dynamique"))


            if isinstance(i, monstre.Boss):
                self.canevas.create_oval(i.x - 15, i.y - 15, i.x + 15, i.y + 15, fill="red", tags=("dynamique", "boss"))
                x1 = i.x - 10
                x2 = x1 + 20
                x3 = x1 + (i.vie / monstre.Boss.vie_max * 20)
                self.canevas.create_rectangle(x1, i.y - 15, x2, i.y - 10, fill="red", tags="dynamique")
                self.canevas.create_rectangle(x1, i.y - 15, x3, i.y - 10, fill="green", tags="dynamique")

    def afficher_tours(self):
        for i in self.modele.liste_tours:
            if isinstance(i, tour.Tour_Sniper):
                self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                              i.y + i.demie_taille, fill="black", tags="dynamique")
                self.canevas.create_oval(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                         i.y + i.demie_taille, fill="grey", tags="dynamique")
            if isinstance(i, tour.Tour_Poison):
                self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                              i.y + i.demie_taille, fill="Purple", tags="dynamique")
                self.canevas.create_oval(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                         i.y + i.demie_taille, fill="green", tags="dynamique")
            if isinstance(i, tour.Tour_Glace):
                self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                              i.y + i.demie_taille, fill="blue", tags="dynamique")
                self.canevas.create_oval(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                         i.y + i.demie_taille, fill="lightblue", tags="dynamique")
            if isinstance(i, tour.Tour_Mitraillette):
                self.canevas.create_rectangle(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                              i.y + i.demie_taille, fill="lightblue", tags="dynamique")
                self.canevas.create_oval(i.x - i.demie_taille, i.y - i.demie_taille, i.x + i.demie_taille,
                                         i.y + i.demie_taille, fill="blue", tags="dynamique")
                self.canevas.create_oval(i.x - i.rayon, i.y - i.rayon, i.x + i.rayon, i.y + i.rayon, fill="",
                                         outline="",
                                         tags="dynamique")

            self.canevas.create_oval(i.x - i.rayon, i.y - i.rayon, i.x + i.rayon, i.y + i.rayon, fill="",
                                     tags="dynamique")

            if len(i.liste_projectiles) != 0:
                for j in i.liste_projectiles:
                    if isinstance(i, tour.Tour_Bombe):
                        self.canevas.create_oval(j.x - 10, j.y - 10, j.x + 10, j.y + 10,
                                                 fill="darkred", tags="dynamique")
                    elif isinstance(i, tour.Tour_Mitraillette):
                        self.canevas.create_oval(j.x - 5, j.y - 5, j.x + 5, j.y + 5,
                                                 fill="blue", tags="dynamique")
                    elif isinstance(i, tour.Tour_Sniper):
                        self.canevas.create_rectangle(j.x - 5, j.y - 5, j.x + 5, j.y + 5,
                                                      fill="darkred", tags="dynamique")

    def afficher_fin_partie(self):
        self.canevas.delete("dynamique")
        self.var_argent.set(str(self.modele.argent) + "$")
        self.var_score.set(self.modele.pointage)
        self.var_vie.set(self.modele.vie)
        self.var_vague.set(self.modele.vague)

        print("fin de partie")


class Modele:
    def __init__(self, parent):
        self.tour_en_cours = ''
        self.parent = parent
        self.largeur_carte = 1200
        self.hauteur_carte = 800
        self.path = [[200, 450], [200, 200], [440, 200], [440, 520], [760, 520], [760, 370], [1250, 370]]
        self.fin_de_partie = 1
        self.delai_creation_creep = 0
        self.nb_creep_vague = 10
        self.delai_creation_creep_max = 20
        self.pointage = 0
        self.argent = 1000
        self.score = 0
        self.vie = 3
        self.vague = 0
        self.liste_monstres_terrain = []
        self.liste_monstres_entrepot = []
        self.liste_projectiles = []
        self.liste_tours = []
        self.animations = {}

    def jouer_partie(self):
        self.bouger_monstres()
        self.attaque_monstres()
        self.verifier_etat_monstre()
        self.verifier_etat_joueur()
        return self.fin_de_partie

    def creer_monstre(self):
        self.vague += 1
        vitesse = 4 * self.vague
        vie = 100 + self.vague * 20

        if self.vague == 10:
            self.liste_monstres_terrain.append(monstre.Boss(-10, 450, vitesse, 1000))
        for i in range(self.nb_creep_vague * self.vague):
            self.liste_monstres_entrepot.append(monstre.Monstre(-10, 450, vitesse, vie))
        self.delai_creation_creep = 0

    def bouger_monstres(self):

        self.spawn_monstre()

        for i in self.liste_monstres_terrain:
            i.avancer_monstre(self.path)

        if not self.liste_monstres_entrepot and not self.liste_monstres_terrain:
            self.creer_monstre()

    def spawn_monstre(self):
        self.delai_creation_creep += 1
        if self.delai_creation_creep == self.delai_creation_creep_max and len(self.liste_monstres_entrepot) != 0:
            temp = self.liste_monstres_entrepot.pop(0)
            self.liste_monstres_terrain.append(temp)
            self.delai_creation_creep = 0

    def attaque_monstres(self):
        for i in self.liste_tours:
            i.action(self.liste_monstres_terrain)

    def creer_tour(self, event):

        x = event.x
        y = event.y

        if self.tour_en_cours == 'S':
            self.argent -= tour.Tour_Sniper.prix
            self.liste_tours.append(tour.Tour_Sniper(x, y, 250, 10))
            self.tour_en_cours = None
        elif self.tour_en_cours == 'P':
            self.argent -= tour.Tour_Poison.prix
            self.liste_tours.append(tour.Tour_Poison(x, y, 100, 10))
            self.tour_en_cours = None
        elif self.tour_en_cours == 'G':
            self.argent -= tour.Tour_Glace.prix
            self.liste_tours.append(tour.Tour_Glace(x, y, 10))
            self.tour_en_cours = None
        elif self.tour_en_cours == 'B':
            self.argent -= tour.Tour_Bombe.prix
            self.liste_tours.append(tour.Tour_Bombe(x, y, 100, 10))
            self.tour_en_cours = None

    def verifier_etat_monstre(self):
        for i in self.liste_monstres_terrain:
            if i.vie <= 0:
                self.pointage += 5
                self.score += 50
                self.argent += 50
                self.liste_monstres_terrain.remove(i)
            if i.x > 1143:
                self.liste_monstres_terrain.remove(i)
                if self.vie > 0:
                    self.vie -= 1
            if i.empoisonne:
                i.vie -= tour.Tour_Poison.degat

    def verifier_etat_joueur(self):
        if self.vie == 0:
            self.parent.partie_en_cours = 0
            self.fin_de_partie = 0

    def jouer_tour(self):
        for i in self.animations:
            self.animations[i].jouer_tour()

    def creer_anim(self, info_gif):
        nom_gif, listeimages = info_gif
        self.animations[nom_gif] = Animer_gif(self, listeimages, 1143, 350)

    def reinitialiser(self):
        self.liste_monstres_terrain = []
        self.liste_monstres_entrepot = []
        self.liste_projectiles = []
        self.liste_tours = []
        self.vie = 3
        self.vague = 0
        self.pointage = 0
        self.fin_de_partie = 1
        self.argent = 1000

    def creer_sniper(self):
        self.tour_en_cours = 'S'

    def creer_poison(self):
        self.tour_en_cours = 'P'

    def creer_bombe(self):
        self.tour_en_cours = 'B'

    def creer_glace(self):
        self.tour_en_cours = 'G'


class Controleur:
    def __init__(self):
        self.partie_en_cours = 0

        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.afficher_debut_partie()
        self.vue.root.mainloop()

    def debuter_partie(self):
        if not self.partie_en_cours:
            self.partie_en_cours = 1
            self.jouer_partie()

    def jouer_partie(self):
        if self.partie_en_cours:
            rep = self.modele.jouer_partie()
            if rep:

                self.modele.jouer_tour()
                self.vue.afficher_partie()
                self.vue.root.after(40, self.jouer_partie)
            else:
                self.vue.afficher_fin_partie()
                self.partie_en_cours = 0
                self.modele.reinitialiser()

    def creer_tour(self, event):
        if self.partie_en_cours:
            self.modele.creer_tour(event)

    def creer_tour_glace(self):
        if self.partie_en_cours:
            self.modele.creer_glace()

    def creer_tour_sniper(self):
        if self.partie_en_cours:
            self.modele.creer_sniper()

    def creer_tour_poison(self):
        if self.partie_en_cours:
            self.modele.creer_poison()

    def creer_anim(self, info_gif):
        self.modele.creer_anim(info_gif)


if __name__ == '__main__':
    c = Controleur()
    print("L'application se termine")
