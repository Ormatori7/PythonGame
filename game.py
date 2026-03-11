from db_init import equipe_col, ennemis_col
import random
from utils import pause


def preparerCombat():
    # on recup tt les heros de l'equipe en utilisant list pour transformer les données en list python
    equipe = list(equipe_col.find())
    return equipe


def VagueCombat():
    vagueActuel = 1
    equipe = preparerCombat()
    # on stock le monstre spawner
    monstre = spawnRandomMonstre()
    vieMonstre = monstre["hp"]
    defenseMonstre = monstre["def"]
    NomMonstre = monstre["nom"]
    AttaqueMonstre = monstre["atk"]
    # tant qu'il reste des héro disponible
    while len(equipe) > 0:
        # on annonce le début de la vague et le numéro
        print(f"======= La vague n°{vagueActuel} va commencer =======")
        pause()
        print(f"le monstre choisi est {NomMonstre}")
        # on appelle la logique combatLogique
        victoire = combatLogique(equipe, vieMonstre, defenseMonstre, AttaqueMonstre)
        # si victoire alors
        if victoire:
            # on affiche la vague
            print(f"======= La vague n°{vagueActuel} a été repousser =======")
            # on appelle la fonction d'incrementation de la vague
            vagueActuel = vagueIncrementation(vagueActuel)
            # appeller fonction pour choisi un nouveau monstre
        # sinon
        else:
            # on appelle la fonction FinCombat
            print("fin du combat")
            FinCombat()
            break


# monstre["atk"]         equipe[0]["hp"] -= 50
def combatLogique(equipe, vieMonstre, defenseMonstre, atk_Monstre):
    # on check si toujours en vie et on return true false pour la condition d'aprés
    while vieMonstre > 0 and CheckEquipeToujoursEnVie(equipe):
        # pour chaque héro dans l'equipe
        for hero in equipe:
            # les héro attaque avce fonction Attaque
            vieMonstre = AttaqueLeMonstre(hero, vieMonstre, defenseMonstre)
            # si le monstre est toujours en vie
            if vieMonstre <= 0:
                return True
            # attaque un hero random de l'equipe si a survecu
            pause()
        # monstre attaque qlq aléatoirement avec fonction Attaque
        AttaqueRandomHero(atk_Monstre, equipe)

        Equipe_en_vie = CheckEquipeToujoursEnVie(equipe)
        if Equipe_en_vie:
            print("l'equipe a survecu au combat")
        else:
            print("l'equipe n'as pas survecu")
            pause()
            pause()
            return False

            # si qlq est mort on tchek si c'est un des héros
            # si oui alors
            # on tcheck si il reste des héros
            # si oui alors
            # on appelle la fonction pour retirer le hero mort de l'equipe
            # si non alors
            # on return false
            # si non
            # on return True (victoire lors de la vague)
    else:
        return False


def AttaqueLeMonstre(attaquant, vieMonstre, defenseMonstre):
    degat = attaquant["atk"]
    # retirer vie en sa basant sur value de l'attaque
    # le zero pour eviter de se faire soigner par defense
    degats_subis = max(0, degat - defenseMonstre)
    Vie_restante = vieMonstre - degats_subis
    if Vie_restante < 0:
        Vie_restante = 0
    print(
        f"Le monstre subit {degat} degats mais reduit les degats de {defenseMonstre} et finit avec {Vie_restante} de vie"
    )
    return Vie_restante


def AttaqueRandomHero(atk_Monstre, equipe):
    hero_Choisi = chooseRandomhero(equipe)
    hero_vie = hero_Choisi["hp"]
    hero_defense = hero_Choisi["def"]
    heroNom = hero_Choisi["nom"]
    print(f"le monster attaque le {heroNom} de {atk_Monstre} degats")
    pause()
    print()
    VieRestante = hero_vie - max(0, atk_Monstre - hero_defense)
    # hero_Choisi.update_one({"hp" : 100}, {"set$":{ "hp": VieRestante}}) # pour la db
    # changer les hp du hero dans l'array equipe
    hero_Choisi["hp"] = VieRestante
    CheckHeroToujoursEnVie(hero_Choisi, equipe)

    return

    # on passe le resultat a la fonction herotoujoursEnvie
    # si pas de vie alors retire hero de la liste


def CheckHeroToujoursEnVie(hero_choisi, equipe):
    if hero_choisi["hp"] <= 0:
        print(f"le hero {hero_choisi["nom"]} est mort")
        retirerHeromort(hero_choisi, equipe)
    else:
        print(f"le hero {hero_choisi["nom"]} a maintenant {hero_choisi["hp"]} de vie")
    # pour le hero attaqué, check sa vie, si c'est <= 0 alors:
    # appeller la fonction retirerHeroMort
    return


def retirerHeromort(hero_choisi, equipe):
    equipe.remove(hero_choisi)
    #  heroInfo = personnages_col.find_one({"nom": hero_choisi})
    # personnages_col.delete_one(heroInfo)
    return


def CheckEquipeToujoursEnVie(equipe):
    # prendre la valeur d'entré pour l'equipe
    for hero in equipe:
        if hero["hp"] > 0:
            return True
        else:
            return False


def FinCombat():
    # recuperer le numéro de la vague
    # ajouter dans la partie classement a coté du nom
    return


def vagueIncrementation(vague):
    # en entrée mettre 1 au début car on intisalise a la premiere vague
    # ajouter un au numéro de la vague
    NouvelleVague = vague + 1
    return NouvelleVague


def spawnRandomMonstre():
    MonstreChoisi = list(ennemis_col.aggregate([{"$sample": {"size": 1}}]))
    return MonstreChoisi[0]  # on ddit qu'on veu le premier dircectement


def chooseRandomhero(equipe):
    Hero_choisi = random.choice(equipe)
    # list(equipe_col.aggregate([{"$sample": {"size": 1}}]))   pour le faire avec la db
    return Hero_choisi


# changer le monstre choisi random
