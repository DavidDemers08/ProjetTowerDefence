import random


class Monstre:
    vie_max = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 10
        self.index = 0
        self.vie = 100

    def avancer_monstre(self, path):
        # cibleX va représenter le premier composant du vecteur dans le tablau du chemin
        # cibleX va représenter le deuxième composant du vecteur dans le tablau du chemin
        if self.index != len(path):
            cibleX = path[self.index][0]
            # cibleY = path[1]
            cibleY = path[self.index][1]
            if self.x < cibleX:
                self.x = self.x + self.vitesse

            if self.y < cibleY:
                self.y += self.vitesse
            elif self.y > cibleY:
                self.y -= self.vitesse

            if self.y == cibleY and self.x == cibleX:
                self.x = cibleX
                self.y = cibleY
                self.index += 1
