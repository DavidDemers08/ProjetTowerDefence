import helper

class Tour:
    def __init__(self, x, y, rayon,demie_taille):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.demie_taille = demie_taille


    def analyse_rayon(self, monstre):
        if helper.Helper().calcDistance(self.x, self.y, monstre.x, monstre.y) <= self.rayon:
            return True


    def attaque_tour(self,monstre,projectile_list):

        if self.analyse_rayon(monstre):
            projectile_list.append(Projectile(self.x,self.y,monstre.x,monstre.y))



