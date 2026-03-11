from db_init import init_database, db, personnages_col, equipe_col, classement_col
from game import VagueCombat
from utils import pause, cleanScreen


# stocke le lien de la partie characters de ma db dans ma variable character_Dispo
character_Dispo = db[
    "characters"
]  # on le defini au debut comme ca reutilisable partout

# os.system("cls")  to clean the screen


# le choix du player
def choix_Menu():
    while True:
        choix_saisie = input("que voulez vous faire? => :")
        if not choix_saisie.isnumeric():
            print("veuillez renter un chiffre")
            continue
        if int(choix_saisie) == 1:
            # demarer le jeu
            demarrage_jeu()
            break
        if int(choix_saisie) == 2:
            # afficher le classement
            afficherClassemnt()
            pause()
            continue
        if int(choix_saisie) == 3:
            print("Vous avez quitté le jeu")
            quit()
        else:
            # message d'erreur
            print("veuillez selectionner un choix valide")


# hero_Choisi = chooseRandomhero(equipe)
#     hero_vie = hero_Choisi["hp"]
#  classement = classement_col.find().sort("vague", 1).limit(1)

# for i in equipe_col.find({}, {"_id": 0, "id_ref": 0}):
#     print(i)


def afficherClassemnt():
    for i in classement_col.find({}, {"_id": 0}).sort("vague", -1).limit(3):
        if classement_col is None:
            print("pas encore de classement")
        else:
            print(i)


# le choix du pseudo
def choix_Nom(min_longeur, max_longeur):
    print(
        f"===== Choissisez un nom entre {min_longeur} et {max_longeur} charactere ======"
    )
    while True:
        saisieNom = input("votre nom => : ")
        if pseudoValide(saisieNom, min_longeur, max_longeur):
            return saisieNom

        else:
            print(
                f"veuillez saisir un pseudo entre {min_longeur} et {max_longeur} charactere"
            )


def personnage_Disponible():
    print(
        f"=========nombre de héros dipsonible: {character_Dispo.count_documents({})} ============"
    )  # count => specifique a monogoDb car la c'est un object
    # afficher ma liste de héros
    for character in character_Dispo.find(
        {}, {"_id": 0, "id_ref": 0}
    ):  # pour dire de cacher le champ id/id ref (0 pour false)
        print(character)


def choose_Hero(heroRestant, pseudo):
    while heroRestant > 0:
        personnage_Disponible()
        print(
            f"=========choissisez 3 héro: nombre de héros restant a selectionner => {heroRestant} ==========="
        )
        SelectionHero()
        heroRestant -= 1
        pause()
        cleanScreen()
    presentationEquipe()
    pause()
    VagueCombat(pseudo)


def presentationEquipe():
    print("Voici votre Equipe:")
    for i in equipe_col.find({}, {"_id": 0, "id_ref": 0}):
        print(i)


def SelectionHero():
    while True:  # la logiqeu de la boucle infinie
        hero_choisi = input("entrer le nom du héro : ")
        # aller chercher la ligne en elle mme pour le nom choisi pour prendre ttes les stats
        heroInfo = personnages_col.find_one({"nom": hero_choisi})
        nomValide = Verification_Hero(hero_choisi)
        if nomValide:
            print(f"------{hero_choisi} a été ajouté a votre equipe-----")
            AjouterHeroEquipe(heroInfo)
            return hero_choisi
        else:
            print(
                f"<<<<<le héro -{hero_choisi}- n'est pas disponible, veuillez selection de nouveau>>>>>"
            )


def AjouterHeroEquipe(heroInfo):
    # ajouté character de db.character a db.equipe avec insert et delete
    equipe_col.insert_one(heroInfo)
    personnages_col.delete_one(heroInfo)


def Verification_Hero(hero_choisi):
    heroPresent = character_Dispo.find_one(
        {"nom": hero_choisi}
    )  # find pour verifier si ce qu'on a ecrit correspond a un nom de la table et nom pour préciser qu'on veut uniquement le nom pour la compraison
    if heroPresent:
        return True
    else:
        return False


# la creation de l'equipe
def menu_Creation_Equipe(pseudo):
    cleanScreen()
    # choisir un heros depuis ma database
    choose_Hero(3, pseudo)


# la validité du pseudo
def pseudoValide(saisieNom, min_longeur, max_longeur):
    if saisieNom.isnumeric():
        print("Veuillez renter des charactere, pas des chiffres")
        return False
    if len(saisieNom) < min_longeur:
        return False
    if len(saisieNom) > max_longeur:
        return False
    return True


def demarrage_jeu():
    cleanScreen()
    # choisir un nom de personnage
    pseudo = choix_Nom(3, 10)
    # creation de l'equipe
    menu_Creation_Equipe(pseudo)


# fonction principale
def Menu():
    init_database()
    # afficher les choix disponnibles
    print("appuie sur 1 pour demarer le jeu")
    print("appuie sur 2 pour afficher le classement")
    print("appuie sur 3 pour quitter")
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
