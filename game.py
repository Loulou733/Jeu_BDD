#on import random
# on import floor de math

#fonction game():
    # vague = 0
    # on trouve un monstre avec random
    # tant que tous les perso ne sont pas mort:
        
        # on attaque l'empire (les personnages attaque le monstre ptetre faire une fonction attaquer)
            # COMMENT 
            # si def monstre < atk perso
                # atk = atk - def
                # hp = hp - atkc
        #si les pv du monstre = 0
            # victoire
            # vague =  vague +1
            #nouveau monstre avec random

        # l'empire contre attaque (le monstre attaque un perso random dans ceux qui sont vivant on lui dmd de choisir un nombre entre 1 et 3)
        # on fais math.floor(random*3) pour avoir un nombre entier entre 1 et 3

        #si les pv de tout les perso = 0
            # defaite
            # on enregistre vague dans la bdd
            # on affcihe le resultat et le classementles pv de tout les perso = 0

from pymongo import MongoClient
import random
from utils import creer_equipe, recuperer_oiseaux, recuperer_cochon
client = MongoClient('mongodb://localhost:27017/')

def choisir_nom():
    return input("Choississez un nom : \n")

def choisir_cochon_actuel():
    return random.choice(recuperer_cochon())


def game():
    nom_du_joueur = choisir_nom()
    cochon = choisir_cochon_actuel()
    derouelement_de_la_vague()