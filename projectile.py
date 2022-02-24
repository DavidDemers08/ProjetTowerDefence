import helper


class Projectile(object):
    def __init__(self, x, y, degat, monstre):
        self.x = x
        self.y = y
        self.degat = degat
        self.vitesse = 20
        self.monstre = monstre
        self.delai = 0

    def lancer_projectile(self):
        self.delai += 1
        distance = helper.Helper.calcDistance(self.x, self.y, self.monstre.x, self.monstre.y)
        if distance > 0:
            angle = helper.Helper.calcAngle(self.x, self.y, self.monstre.x, self.monstre.y)
            cible = helper.Helper.getAngledPoint(angle, self.vitesse, self.x, self.y)
            self.x = cible[0]
            self.y = cible[1]

    def atteindre_cible(self,liste_monstre = []):
        isDead = False
        if self.monstre is None:
            isDead = True

        cibleX = self.monstre.x
        cibleY = self.monstre.y
        if (cibleX + 12 >= self.x >= cibleX - 12) and (cibleY + 12 >= self.y >= cibleY - 12):
            isDead = True
            self.monstre.vie -= self.degat

        return isDead


class Projectile_Bombe(Projectile):
    def __init__(self, x, y, degat, monstre):
        Projectile.__init__(self, x, y, degat, monstre)
        self.rayon = 100

    def atteindre_cible(self,liste_monstre):
        isDead = False

        if self.monstre is None:
            isDead = True

        cibleX = self.monstre.x
        cibleY = self.monstre.y
        if (cibleX + 12 >= self.x >= cibleX - 12) and (cibleY + 12 >= self.y >= cibleY - 12):
            isDead = True
            explosion_list = self.explosion(liste_monstre)
            for monstre_bombe in explosion_list:
                monstre_bombe.vie -= self.degat

        return isDead

    def explosion(self,monstre_list):
        explosion_list = []
        for monstre in monstre_list:
            if helper.Helper().calcDistance(self.x, self.y, monstre.x, monstre.y) <= self.rayon:
                explosion_list.append(monstre)
        return explosion_list
