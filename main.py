from utils import afficher_le_menu

MENU = [
  "Lancer Jeu",
  "Afficher les scores",
  "Quitter",
   ]

def choix(option : list):
    choix_user : int = input("Choississez un nombre entre 1 et 3")
    verifier_choix(choix_user=, option)

def verifier_choix(choix_user, option : list):
    if (min <= choix_user <= max):
        return choix_user
    else:
        raise ValueError("Veuillez mettre un choix valide entre 1 et 3")
    






def main():
    for element in MENU:
        print(element)
    while True:
        choix(MENU)

    if choix_user == 1:
        game()
    if choix_user == 2:
        afficher_le_menu()
    else:
        sys.exit()
    
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur
# Process
#    JEU
#    Afficher les scores
#        Recuperer scores base
#            ouvrir base
#            acceder a collection score
#            find
#            convertir curseur en list
#        filtrer les 3 meilleurs
#             trie le tableau sur element.waves
#             prendre 3 derniers elements
#                    array[-3:-1]
#        Affiche les score
#    Quitter
#       sys.exit()



    