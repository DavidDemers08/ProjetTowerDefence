from tkinter import *

class Vue():
    def __init__(self,parent):
        self.parent = parent
        self.root = Tk()
        self.root.title("TowerDefence 0.1")

class Modele():
    def __init__(self,parent):
        self.parent = parent


class Controleur():
    def __init__(self):
        self.vue = Vue(self)
        self.modele = Modele(self)
        self.vue.root.mainloop()



if __name__ == '__main__':
    c = Controleur()
    print("Fin du programme")
