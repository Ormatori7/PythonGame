import pymongo
import random
from db_init import init_database, db


# stocke le lien de la partie characters de ma db dans ma variable character_Dispo
character_Dispo = db[
    "characters"
]  # on le defini au debut comme ca reutilisable partout


# le choix du player
def choix_Menu():
    init_database
    choix_saisie = input()
    if int(choix_saisie) == 1:
        # demarer le jeu
        demarrage_jeu()
    if int(choix_saisie) == 2:
        # afficher le classement
        print("affichage classement")
    if int(choix_saisie) == 3:
        print("Vous avez quitté le jeu")
        quit()
    else:
        # message d'erreur
        print("veuillez selectionner un choix valide")


# le choix du pseudo
def choix_Nom(min_longeur, max_longeur):
    print(f"Choissisez un nom entre {min_longeur} et {max_longeur} charactere")
    while True:
        saisieNom = input()
        if pseudoValide(saisieNom, min_longeur, max_longeur):
            return saisieNom

        else:
            print(
                f"veuillez saisir un pseudo entre {min_longeur} et {max_longeur} charactere"
            )


def personnage_Disponible():
    print(
        f"=========nombre de héros dipsonible: {character_Dispo.count_documents({})} ============"
    )  # count => specifique a monogoDb car la c'est une object
    # afficher ma liste de héros
    for character in character_Dispo.find(
        {}, {"_id": 0}
    ):  # pour dire de cacher le champ id (0 pour false)
        print(character)


def choose_Hero(heroRestant):
    while heroRestant > 0:
        personnage_Disponible()
        print(
            f"=========choissisez 3 héro: nombre de héros restant a selectionner => {heroRestant} ==========="
        )
        SelectionHero()
        heroRestant -= 1


def SelectionHero():
    while True:  # la logiqeu de la boucle infinie
        hero_choisi = input("entrer le nom du héro : ")
        nomValide = Verification_Hero(hero_choisi)
        if nomValide:
            print(f"------{hero_choisi} a été ajouté a votre equipe-----")
            return hero_choisi
        else:
            print(
                f"<<<<<le héro -{hero_choisi}- n'est pas disponible, veuillez selection de nouveau>>>>>"
            )


def Verification_Hero(hero_choisi):
    heroPresent = character_Dispo.find_one(
        {"nom": hero_choisi}
    )  # find pour verifier si ce qu'on a ecrit correspond a un nom de la table et nom pour préciser qu'on veut uniquement le nom pour la compraison
    if heroPresent:
        return True
    else:
        return False


# la creation de l'equipe
def menu_Creation_Equipe():
    # boucle pour mes trois heros
    # choisir un heros depuis ma database
    choose_Hero(3)


# la validité du pseudo
def pseudoValide(saisieNom, min_longeur, max_longeur):
    if saisieNom.isnumeric():
        return False
    if len(saisieNom) < min_longeur:
        return False
    if len(saisieNom) > max_longeur:
        return False
    return True


def demarrage_jeu():
    # initialiser la database
    # choisir un nom de personnage
    choix_Nom(3, 7)
    # creation de l'equipe
    menu_Creation_Equipe()


# fonction principale
def Menu():
    # afficher les choix disponnibles
    print("entre sur 1 pour demarer le jeu")
    print("entre sur 2 pour afficher le classement")
    print("entre sur 3 pour quitter")
    choix_Menu()


# lancer la fonction
Menu()


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
