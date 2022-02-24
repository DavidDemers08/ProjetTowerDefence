import random


class Monstre(object):
    vie_max = 100
    prix = 20
    point = 50
    vitesse = 2


    def __init__(self, x, y, vitesse, vie):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.index = 0
        self.vie = vie
        self.empoisonne = False

    def avancer_monstre(self, path):
        if self.index != len(path):
            cibleX = path[self.index][0]
            cibleY = path[self.index][1]
            if self.x < cibleX:
                self.x = self.x + self.vitesse

            if self.y < cibleY:
                self.y += self.vitesse
            elif self.y > cibleY:
                self.y -= self.vitesse

            if cibleX-2 <= self.x <= cibleX+2 and cibleY-2 <= self.y <= cibleY+2:
                self.x = cibleX
                self.y = cibleY
                self.index += 1




class Boss(Monstre):
    vie_max = 200

    def __init__(self, x, y, vitesse, vie):
        super().__init__(x, y, vitesse, vie)

    def avancer_monstre(self, path):
        super().avancer_monstre(path)
