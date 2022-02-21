

class Animer_gif():
    def __init__(self,parent,listeimages):
        self.parent = parent
        self.images = listeimages
        self.x = 1143
        self.y = 350
        self.max_image = len(self.images)
        self.indice = 0

    def jouer_tour(self):
        self.indice+=1
        if self.indice == self.max_image:
            self.indice=0

