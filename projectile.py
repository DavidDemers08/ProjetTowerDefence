import helper
class Projectile:
    def __init__(self,x,y,degat,monstre):
        self.x = x
        self.y = y
        self.degat= degat
        self.vitesse = 20
        self.monstre = monstre
        self.delai = 0

    def lancer_projectile(self):

        self.delai += 1
        distance = helper.Helper.calcDistance(self.x, self.y, self.monstre.x,self.monstre.y)
        if distance > 0:
            angle = helper.Helper.calcAngle(self.x, self.y, self.monstre.x, self.monstre.y)
            cible = helper.Helper.getAngledPoint(angle, self.vitesse, self.x, self.y)
            self.x = cible[0]
            self.y = cible[1]

    def atteindre_cible(self):
        isDead = False
        if self.monstre is None:
            isDead = True

        cibleX = self.monstre.x
        cibleY = self.monstre.y
        if (cibleX + 12 >= self.x >= cibleX - 12) and (cibleY + 12 >= self.y >= cibleY - 12):
            isDead = True
            self.monstre.vie -= self.degat

        return isDead