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
            if monstre.x == self.x + self.rayon and monstre.x == self.x - self.rayon:
                pass





