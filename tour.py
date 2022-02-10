import helper

class Tour:
    def __init__(self, x, y, rayon,demie_taille):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.demie_taille = demie_taille

    def emplacement_valide(self):
        pass

    def analyse_rayon(self, monstre_list):
        for monstre in monstre_list:
            if helper.Helper().calcDistance(self.x, self.y, monstre.x, monstre.y) <= self.rayon:
                pass #le monstre est dans le rayon dans la tour






