import random
from tkinter import *

mon_id = 0


def creer_id():
    global mon_id
    mon_id += 1
    return mon_id


class Toto():
    def __init__(self, parent, id, couleur):
        self.parent = parent
        self.x = random.randrange(600)
        self.y = random.randrange(400)
        self.id = id
        self.couleur = couleur


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.dico_toto = {}

    def creer_toto(self):
        c = ["red", "yellow", "pink", "green", "purple"]
        for i in range(3):
            id = creer_id()
            coul = random.choice(c)
            c.remove(coul)
            t = Toto(self, id, coul)
            self.dico_toto[id] = t

    def trouver_toto(self, id):
        objet = self.dico_toto[id]
        return objet.x, objet.y


class Vue():
    def __init__(self, parent):
        self.parent = parent
        self.root = Tk()
        self.canevas = Canvas(self.root, width=600, height=400, bg="blue")
        self.canevas.pack()
        self.canevas.bind("<Button-3>", self.parent.creer_toto)
        self.canevas.tag_bind("toto", "<Button-1>", self.trouver_toto)

    def afficher_toto(self, dico_toto):
        for i in dico_toto:
            i = dico_toto[i]
            self.canevas.create_oval(i.x - 10, i.y - 10, i.x + 10, i.y + 10, fill=i.couleur,
                                     tags=(i.id, "toto"))

    def trouver_toto(self, evt):
        val = self.canevas.gettags(CURRENT)
        print(val)
        self.parent.trouver_toto(val[0])


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.root.mainloop()

    def creer_toto(self, event):
        self.modele.creer_toto()
        self.vue.afficher_toto(self.modele.dico_toto)

    def trouver_toto(self, id):
        self.modele.trouver_toto(id)


if __name__ == '__main__':
    c = Controleur()
