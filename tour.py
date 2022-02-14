import helper
import projectile

class Tour:
    def __init__(self, x, y, rayon, demie_taille):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.demie_taille = demie_taille
        self.delai_tire = 0
        self.liste_projectiles = []
        self.vitesse_attaque = 10
        # mitraillette vitesse = 2

    def analyse_rayon(self, monstre):
        if helper.Helper().calcDistance(self.x, self.y, monstre.x, monstre.y) <= self.rayon:
            return True

    def attaque(self, liste_monstre):
        ciblex = 0
        cibley = 0
        self.delai_tire += 1
        for monstre in liste_monstre:
            if monstre.x > ciblex:
                ciblex = monstre.x
                cibley = monstre.y
            if self.analyse_rayon(monstre) and self.delai_tire >= self.vitesse_attaque:
                self.liste_projectiles.append(projectile.Projectile(self, monstre))
                self.delai_tire = 0
            if len(self.liste_projectiles) != 0:
                for i in self.liste_projectiles:
                    i.cibleX = ciblex
                    i.cibleY = cibley

        self.lancer_projectiles()

    def lancer_projectiles(self):
        if len(self.liste_projectiles) != 0:
            for projectile in self.liste_projectiles:
                projectile.lancer_projectile()
                if (projectile.cibleX + 5 >= projectile.x >= projectile.cibleX - 5) and (projectile.cibleY +5 >= projectile.y >= projectile.cibleY - 5):
                    self.liste_projectiles.remove(projectile)