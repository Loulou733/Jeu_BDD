# def choisir les personnages ou un personnage 
# 



#fonction attaque avec 2 param (attaquant, attaqué):
    # on calcul si l'attaque et superieur avec la defense de l'attaqué
    # si l'attaque est superieur
        # on prend le reste et on lui enleve les hp
    #sinon
        #on lui enleve pas de hp

#fonction afficher le menue
    #print(...)

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client.JeuBDD
collection = db.monsters

MENU = [
  "Lancer Jeu",
  "Afficher les scores",
  "Quitter",
   ]

def recuperer_oiseaux():
    client = MongoClient("mongodb://localhost:27017")
    db = client["JeuBDD"]
    collection = db["birds"]

    cursor = collection.find()
    oiseaux = list(cursor)

def recuperer_cochon():
    client = MongoClient("mongodb://localhost:27017")
    db = client["JeuBDD"]
    collection = db["pigs"]

    cursor = collection.find()
    cochons = list(cursor)

def choix(option):
    choix_user = input(f"Choississez un nombre entre 1 et 3")
    choix_user = int(choix_user)
    if (1 <= choix_user <= 3):
        return choix_user
    else:
        raise ValueError("Veuillez mettre un choix valide entre 1 et 3")
    

def afficher_les_scores():
    scores = list(db["scores"].find().sort("waves", -1).limit(3))
    for perso in scores:
        print(f"- {perso['player_name']}: {perso['waves']} vagues")

def afficher_oiseaux(oiseaux):
    print("Oiseaux")
    i = 1
    for oiseau in oiseaux:
        print(f"{i}. {oiseau.nom} (ATK: {oiseau.attaque}, DEF: {oiseau.defense}, PV: {oiseau.vie})")
        i += 1

def oiseaux_disponibles(oiseaux, equipe):
    disponibles = []
    for oiseau in oiseaux:
        if oiseau not in equipe:
            disponibles.append(oiseau)
    return disponibles

def creer_equipe(oiseaux):
    equipe = []
    while not equipe == len(3):
        disponibles = oiseaux_disponibles(oiseaux, equipe)
        afficher_oiseaux(disponibles)
        print("Choisis un oiseau:")
        choix = int(input())
        if choix < 1 or choix > len(disponibles):
            print("Choix invalide")
            continue
        equipe.append(disponibles[choix - 1])
    return equipe
