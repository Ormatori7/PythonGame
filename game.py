from db_init import equipe_col, ennemis_col, classement_col
import random
from utils import pause, cleanScreen


def preparerCombat():
    # on recup tt les heros de l'equipe en utilisant list pour transformer les données en list python
    equipe = list(equipe_col.find())
    return equipe


def VagueCombat(pseudo):
    cleanScreen()
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
        AnnoncerInfo(vagueActuel, NomMonstre)
        victoire = combatLogique(
            equipe, vieMonstre, defenseMonstre, AttaqueMonstre, NomMonstre
        )
        # si victoire alors
        if victoire:
            # on affiche la vague
            infoNouvelleVague(vagueActuel)
            # on appelle la fonction d'incrementation de la vague
            vagueActuel = vagueIncrementation(vagueActuel)
            Nouveaumonstre = spawnRandomMonstre()
            vieMonstre = Nouveaumonstre["hp"]
            defenseMonstre = Nouveaumonstre["def"]
            NomMonstre = Nouveaumonstre["nom"]
            AttaqueMonstre = Nouveaumonstre["atk"]
            # appeller fonction pour choisi un nouveau monstre
        # sinon
        else:
            # on appelle la fonction FinCombat
            FinCombat(vagueActuel, pseudo)
            break


def AnnoncerInfo(vagueActuel, NomMonstre):
    # on annonce le début de la vague et le numéro
    print(f"======= La vague n°{vagueActuel} va commencer =======")
    pause()
    print(f"-----le monstre choisi est {NomMonstre}----------")
    pause()
    cleanScreen()
    # on appelle la logique combatLogique


def infoNouvelleVague(vagueActuel):
    print(f"======= La vague n°{vagueActuel} a été repousser =======")
    pause()
    pause()
    cleanScreen()


def combatLogique(equipe, vieMonstre, defenseMonstre, atk_Monstre, NomMonstre):
    # on check si toujours en vie et on return true false pour la condition d'aprés
    while vieMonstre > 0 and CheckEquipeToujoursEnVie(equipe):
        # pour chaque héro dans l'equipe
        for hero in equipe:
            # les héro attaque avce fonction Attaque
            vieMonstre = AttaqueLeMonstre(hero, vieMonstre, defenseMonstre, NomMonstre)
            # si le monstre est toujours en vie
            if vieMonstre <= 0:
                return True
            # attaque un hero random de l'equipe si a survecu
            pause()
        cleanScreen()
        # monstre attaque qlq aléatoirement avec fonction Attaque
        AttaqueRandomHero(atk_Monstre, equipe, NomMonstre)
        Equipe_en_vie = CheckEquipeToujoursEnVie(equipe)
        if Equipe_en_vie:
            InfoContinuerCombat()
        else:
            InfoTerminerCombat()
            return False
    else:
        return False


def InfoContinuerCombat():
    pause()
    cleanScreen()
    print("l'equipe continue d'attaquer")
    pause()
    cleanScreen()


def InfoTerminerCombat():
    print("l'equipe n'as pas survecu")
    pause()
    pause()
    cleanScreen()


def AttaqueLeMonstre(attaquant, vieMonstre, defenseMonstre, nomMonstre):
    degat = attaquant["atk"]
    nomHero = attaquant["nom"]
    # retirer vie en sa basant sur value de l'attaque
    # le zero pour eviter de se faire soigner par defense
    degats_subis = max(0, degat - defenseMonstre)
    Vie_restante = vieMonstre - degats_subis
    if Vie_restante < 0:
        Vie_restante = 0
        print("======= le monstre est mort =======")
    else:
        print(f"{nomHero} attaque {nomMonstre}")
        pause()
        print(
            f"Le {nomMonstre} subit {degat} degats mais reduit les degats de {defenseMonstre} et finit avec {Vie_restante} de vie"
        )

    return Vie_restante


def AttaqueRandomHero(atk_Monstre, equipe, NomMonstre):
    hero_Choisi = chooseRandomhero(equipe)
    hero_vie = hero_Choisi["hp"]
    hero_defense = hero_Choisi["def"]
    heroNom = hero_Choisi["nom"]
    print(f"<<<< {NomMonstre} attaque le {heroNom} de {atk_Monstre} degats >>>>")
    pause()
    cleanScreen()
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
        print(f"~~~~~ le hero {hero_choisi["nom"]} est mort ~~~~~")
        retirerHeromort(hero_choisi, equipe)
    else:
        print(
            f">>>>>> le hero {hero_choisi["nom"]} a maintenant {hero_choisi["hp"]} de vie >>>>>>"
        )
    # pour le hero attaqué, check sa vie, si c'est <= 0 alors:
    # appeller la fonction retirerHeroMort
    return


def retirerHeromort(hero_choisi, equipe):
    equipe.remove(hero_choisi)
    # heroInfo = personnages_col.find_one({"nom": hero_choisi})
    # personnages_col.delete_one(heroInfo)
    return


def CheckEquipeToujoursEnVie(equipe):
    # prendre la valeur d'entré pour l'equipe
    for hero in equipe:
        if hero["hp"] > 0:
            return True
        else:
            return False


# {"nom": "le robot", "atk": 10, "def": 5, "hp": 100},


def FinCombat(vagueActuel, pseudo):
    print("fin du combat, votre score a été ajouté au classement")
    score = [{"nom": pseudo, "vague": vagueActuel}]
    classement_col.insert_many(score)
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




