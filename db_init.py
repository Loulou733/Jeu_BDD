from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.JeuBDD
collection = db.monsters

birds = db["birds"]
pigs = db["pigs"]

list_birds = [
    { "name": "Red", "atk": 15, "def": 10, "pv": 100 },
    { "name": "Chuck", "atk": 20, "def": 5, "pv": 80 },
    { "name": "Bomb", "atk": 18, "def": 7, "pv": 90 },
    { "name": "Matilda", "atk": 22, "def": 8, "pv": 85 },
    { "name": "The Blues", "atk": 14, "def": 12, "pv": 110 },
    { "name": "Terrence", "atk": 25, "def": 3, "pv": 75},
    { "name": "Hal", "atk": 17, "def": 15, "pv": 120 },
    { "name": "Bubbles", "atk": 19, "def": 9, "pv": 95 },
]

list_pigs = [
    { "name": "Cochon de base", "atk": 10, "def": 5, "pv": 50 },
    { "name": "Cochon casqué", "atk": 20, "def": 8, "pv": 120 },
    { "name": "Caporal", "atk": 35, "def": 20, "pv": 300 },
    { "name": "Contremaitre", "atk": 12, "def": 6, "pv": 70 },
    { "name": "Chef Cochon", "atk": 25, "def": 15, "pv": 200 },
    { "name": "Roi cochon", "atk": 18, "def": 10, "pv": 100 },
]

for character in list_birds:
    birds.replace_one(
        {"name": character["name"]},
        character,
        upsert=True
    )

for monster in list_pigs:
    pigs.replace_one(
        {"name": monster["name"]},
        monster,
        upsert=True
    )


client.close()
