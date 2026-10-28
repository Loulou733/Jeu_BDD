#class birds:
    #on fais le def init
        #On met tout les stats des oiseaux


#class pigs:
    #on fais le def init
        #On met tout les stats du cochon
class Entite():
    def __init__(self, name, attack, defense, pv):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.pv = pv

    def est_vivant(self):
        return self.pv < 0

    
class birds(Entite):
    pass

class pigs(Entite):
    pass