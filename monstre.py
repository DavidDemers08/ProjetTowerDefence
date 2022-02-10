class Monstre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 3


    def avancer_monstre(self, cibleX, cibleY):
        # cibleX va représenter le premier composant du vecteur dans le tablau du chemin
        # cibleX va représenter le deuxième composant du vecteur dans le tablau du chemin
        if self.x < cibleX - self.vitesse:
            self.x = self.x + self.vitesse
            print("allo")

        if self.y < cibleY - self.vitesse:
            self.y = self.y + self.vitesse

        self.x += self.vitesse

