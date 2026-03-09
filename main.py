import pymongo
import random
from db_init import init_database 


def choix_Menu():
    choix_saisie = input()
    if int(choix_saisie) == 1:
        #demarer le jeu
        demarrage_jeu()
    if int(choix_saisie) == 2:
        #afficher le classement
        print("affichage classement")
    if int(choix_saisie) == 3:
        #quitter le jeu
        print("quitter le jeu")
    else:
        #message d'erreur 
        print("veuillez selectionner un nombre valide")


def choix_Nom(min_longeur, max_longeur):
    print(f"Choissisez un nom entre {min_longeur} et {max_longeur}")
    while True:
        saisieNom = input()
        if pseudoValide(saisieNom, min_longeur, max_longeur):
            print(f"veuillez saisir un pseudo entre {min_longeur} et {max_longeur} charactere")
        else:
            return saisieNom
        print("fonctionne ici")
    


def pseudoValide(saisieNom, min_longeur, max_longeur):
    if saisieNom.isnumeric():
        return False
    if len(saisieNom) < min_longeur:
        return False
    if len(saisieNom) > max_longeur:
        return False
    return True
    
        


def demarrage_jeu():
    #initialiser la database
    # choisir un nom de personnage
    choix_Nom(3, 7)
    # creation de l'equipe
    return


# def recuperer_nombre_valide(min_val, max_val, message):
# #afficher message
#     print(message)

# #tant que vrai
#     while True:

#     saisie = input()
#     if is_invalide(saisie):
#         print(f"Veuillez saisir un nombre entre {min_val} et {max_val}")

#     else:
#         return saisie


# saisie est un nombre?
# def is_valid(saisie):
#     if not saisie.isnumeric():
#         return True
#     else:
#         return False
#     if saisie > max_val:
#         return True


def Menu():
    #afficher les choix disponnibles
    print("entre sur 1 pour demarer le jeu")
    print("entre sur 2 pour afficher le classement")
    print("entre sur 3 pour quitter")

    choix_Menu()

# afficher le classement
# quitter

Menu()
