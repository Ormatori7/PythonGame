import pymongo
import random
import db_init


def choix_Menu():
    print("appuyer sur 1 pour demarer le jeu")
    print("appuyer sur 2 pour afficher le classement")
    print("appuyer sur 3 pour quitter")


def demarrage_jeu():
    

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
def is_valid(saisie):
    if not saisie.isnumeric():
        return True
    else:
        return False
    if saisie > max_val:
        return True


def Menu():
#afficher les choix disponnibles
    choix_Menu()
#demarer le jeu
    demarrage_jeu()
# afficher le classement
# quitter

Menu()
