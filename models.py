#class birds:
    #on fais le def init
        #On met tout les stats des oiseaux


#class pigs:
    #on fais le def init
        #On met tout les stats du cochon


class birds:
    def __init__(self, nom, attaque, defense, vie):
        self.name = nom  
        self.attaque = attaque
        self.defense = defense
        self.vie = vie

    def est_vivant(self):
        self.vie > 0


class pigs:
    def __init__(self, nom, attaque, defense, vie):
        self.name = nom  
        self.attaque = attaque
        self.defense = defense
        self.vie = vie

    def est_vivant(self):
        self.vie > 0