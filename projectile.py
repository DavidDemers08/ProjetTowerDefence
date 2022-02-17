import helper
class Projectile:
    def __init__(self,tour,monstre):
        self.x= tour.x
        self.y =tour.y
        self.vitesse = 20
        self.monstre = monstre
        self.delai = 0

    def lancer_projectile(self):
        self.delai += 1
        distance = helper.Helper.calcDistance(self.x, self.y, self.monstre.x,self.monstre.y)
        if distance > 0:
            angle = helper.Helper.calcAngle(self.x, self.y,self.monstre.x,self.monstre.y)
            cible = helper.Helper.getAngledPoint(angle,self.vitesse,self.x,self.y)
            self.x = cible[0]
            self.y = cible[1]


