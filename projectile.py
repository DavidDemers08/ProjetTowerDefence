class Projectile:
    def __init__(self,tour,monstre):
        self.x=tour.x
        self.y =tour.y
        self.cibleX = monstre.x
        self.cibleY = monstre.y
        self.vitesse = 20

    def lancer_projectile(self):
        if self.x < self.cibleX:
            self.x = self.x + self.vitesse
        elif self.x > self.cibleX:
            self.x -= self.vitesse

        if self.y < self.cibleY:
            self.y += self.vitesse
        elif self.y > self.cibleY:
            self.y -= self.vitesse

        if self.y == self.cibleY and self.x == self.cibleX:
            self.x = self.cibleX
            self.y = self.cibleY


