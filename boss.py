import monstre


class Boss(monstre.Monstre):
    def __init__(self, x, y, vitesse, vie):
        super().__init__(x, y, vitesse, vie)

    def avancer_monstre(self, path):
        super().avancer_monstre(path)