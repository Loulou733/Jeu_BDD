#class birds:
    #on fais le def init
        #On met tout les stats des oiseaux


#class pigs:
    #on fais le def init
        #On met tout les stats du cochon
class Entite():
    def __init__(self, nom, attaque, defense, pv):
        self.nom = nom
        self.attaque = attaque
        self.defense = defense
        self.pv = pv

    def est_vivant(self):
        return self.pv > 0

    def attaquer(self, cible):
        dommage = self.attaque - cible.defense
        dommage = max(1, dommage)
        cible.pv = cible.pv - dommage
        cible.pv = max(0, cible.pv)
        return dommage

    
class birds(Entite):
    pass

class pigs(Entite):
    pass