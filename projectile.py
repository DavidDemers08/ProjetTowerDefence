import helper
class Projectile:
    def __init__(self,tour,monstre):
        self.x= tour.x
        self.y =tour.y
        self.cibleX = monstre.x
        self.cibleY = monstre.y
        self.vitesse = 10
        self.monstre = monstre

    def lancer_projectile(self):

        distance = helper.Helper.calcDistance(self.x, self.y, self.cibleX, self.cibleY)
        if distance > 0:
            angle = helper.Helper.calcAngle(self.x, self.y, self.cibleX, self.cibleY)
            cible = helper.Helper.getAngledPoint(angle,self.vitesse,self.x,self.y)
            self.x = cible[0]
            self.y = cible[1]


