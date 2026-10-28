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
client = MongoClient('mongodb://localhost:27017/')

db = client.JeuBDD
collection = db.monsters

import random 
from math import floor
from models import pigs, birds

def game():
    nom_du_joueur = input("Votre nom :")
    vague = 0
    pipeline = [{"$sample": {"size": 1}}]
    pig_actuel = list(collection.aggregate(pipeline))
    
    while pig.est_vivant():
        if pig.defense < bird.attaque:
            attaque = pig.defense - bird.attaque
            pig.vie = pig.vie - attaque
        if pig.vie <= 0 :
            vague = vague + 1
            pipeline = [{"$sample": {"size": 1}}]
            pig = list(collection.aggregate(pipeline))