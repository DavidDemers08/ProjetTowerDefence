import helper
import projectile
from monstre import Monstre


class Tour(object):
    prix = 400

    def __init__(self, x, y, rayon, demie_taille,vitesse_attaque = 20,degat = 50):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.demie_taille = demie_taille
        self.vitesse_attaque = vitesse_attaque
        self.degat = degat
        self.niveau = 0
        self.delai_tire = 0
        self.liste_projectiles = []


    def analyse_rayon(self, monstre):
        if helper.Helper().calcDistance(self.x, self.y, monstre.x, monstre.y) <= self.rayon:
            return True

    def action(self, liste_monstre):
        self.delai_tire += 1
        for monstre in liste_monstre:
            if self.analyse_rayon(monstre) and self.delai_tire >= self.vitesse_attaque:
                if isinstance(self,Tour_Bombe):
                    self.liste_projectiles.append(projectile.Projectile_Bombe(self.x, self.y, self.degat, monstre))
                elif isinstance(self,Tour_Sniper):
                    self.liste_projectiles.append(projectile.Projectile(self.x, self.y, self.degat, monstre))
                else:
                    self.liste_projectiles.append(projectile.Projectile(self.x, self.y, self.degat, monstre))
                self.delai_tire = 0
        self.lancer_projectiles(liste_monstre)

    def lancer_projectiles(self, liste_monstre):
        if len(self.liste_projectiles) != 0:
            for projectile in self.liste_projectiles:
                projectile.lancer_projectile()
                if projectile.atteindre_cible(liste_monstre):
                    self.liste_projectiles.remove(projectile)


    def upgrade(self):
        self.niveau += 1

class Tour_Glace(Tour):
    prix = 500

    def __init__(self, x, y, demie_taille):
        Tour.__init__(self,x, y, 75, demie_taille)
        self.vitesse_ralentissement = 1

    def action(self, liste_monstre):

        for monstre in liste_monstre:

            if self.analyse_rayon(monstre):
                monstre.vitesse = self.vitesse_ralentissement
            else:
                monstre.vitesse = Monstre.vitesse


class Tour_Sniper(Tour):
    prix = 100

    def __init__(self, x, y, rayon, demie_taille):
        Tour.__init__(self, x, y, rayon, demie_taille, 60, 100)
        self.delai_tire = 0
        self.liste_projectiles = []

    def upgrade(self):
        self.niveau += 1
        if self.niveau == 1:
            pass
        elif self.niveau == 2:
            pass
        elif self.niveau == 3:
            pass

class Tour_Poison(Tour):
    degat = 0.15
    prix = 300

    def __init__(self, x, y, rayon, demie_taille):
        Tour.__init__(self, x, y, rayon, demie_taille)

    def action(self, liste_monstre):
        for monstre in liste_monstre:
            if self.analyse_rayon(monstre):
                monstre.empoisonne = True

    def upgrade(self):
        self.niveau += 1
        if self.niveau == 1:
            pass
        elif self.niveau == 2:
            pass
        elif self.niveau == 3:
            pass


class Tour_Bombe(Tour):
    prix = 600

    def __init__(self, x, y, rayon, demie_taille):
        Tour.__init__(self, x, y, rayon, demie_taille, 60, 100)
        self.delai_tire = 0
        self.liste_projectiles = []

    def upgrade(self):
        self.niveau += 1
        if self.niveau == 1:
            pass
        elif self.niveau == 2:
            pass
        elif self.niveau == 3:
            pass

class Tour_Mitraillette(Tour):
    prix = 200

    def __init__(self, x, y, rayon, demie_taille):
        Tour.__init__(self, x, y, rayon, demie_taille, 2, 5)
        self.delai_tire = 0
        self.liste_projectiles = []

    def upgrade(self):
        self.niveau += 1
        if self.niveau == 1:
            pass
        elif self.niveau == 2:
            pass
        elif self.niveau == 3:
            pass