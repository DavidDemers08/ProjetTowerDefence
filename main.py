from tkinter import *


class Vue():
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


    def afficher_partie(self):
        self.cadre_info.create_rectangle(0, self.modele.hauteur / 2 - 50, self.modele.largeur,
                                         self.modele.hauteur / 2 + 50, fill="beige")


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 1000
        self.hauteur = 800


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.root.mainloop()



if __name__ == '__main__':
    c = Controleur()
    print("Fin du programme")