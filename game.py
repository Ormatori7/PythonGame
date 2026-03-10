from db_init import equipe_col, ennemis_col
import random


def preparerCombat():
    # on recup tt les heros de l'equipe en utilisant list pour transformer les données en list python
    equipe = list(equipe_col.find())
    return equipe


def VagueCombat():
    vagueActuel = 1
    equipe = preparerCombat()
    # tant qu'il reste des héro disponible
    while len(equipe) > 0:
        # on annonce le début de la vague et le numéro
        print(f"======= La vague n°{vagueActuel} va commencer =======")
        # on stock le monstre spawner
        monstre = spawnMonstre()
        print(f"le monstre choisi est {monstre["nom"]}")
        # on appelle la logique combatLogique
        victoire = combatLogique(equipe, monstre)
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
            # print("fin du combat")
            FinCombat()
            break


# monstre["atk"]         equipe[0]["hp"] -= 50
def combatLogique(equipe, monstreref):
    # on check si toujours en vie et on return true false pour la condition d'aprés
    if EquipeToujoursEnVie(equipe):
        # pour chaque héro dans l'equipe
        for hero in equipe:
            # les héro attaque avce fonction Attaque
            vie_Restante_Monstre = AttaqueMonstre(hero, monstreref)
            # si le monstre est toujours en vie
        if vie_Restante_Monstre > 0:
            print("appele ici")
            return

            # monstre attaque qlq aléatoirement avec fonction Attaque
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
        print("il est appele la")
        return False


def EquipeToujoursEnVie(equipe):
    # prendre la valeur d'entré pour l'equipe
    for hero in equipe:
        if hero["hp"] > 0:
            return True
        else:
            return False


def AttaqueMonstre(attaquant, monstreRef):
    degat_a_infliger = attaquant["atk"]    
    vieMonstre = monstreRef["hp"]
    defenseMonstre = monstreRef["def"]
    # print de l'attaque
    # fonction pour pedre de la vie
    vieRestatanteMonstre = subirDegatsMonstre(degat_a_infliger, vieMonstre, defenseMonstre)
    print(f"les hp du return sont de {vieRestatanteMonstre}")
    return vieRestatanteMonstre


def subirDegatsMonstre(Degats, vieMonstre, defenseMonstre):
    # retirer vie en sa basant sur value de l'attaque
    vieMonstre = vieMonstre - (Degats - defenseMonstre)
    return vieMonstre


def FinCombat():
    # recuperer le numéro de la vague
    # ajouter dans la partie classement a coté du nom
    return


def vagueIncrementation(vague):
    # en entrée mettre 1 au début car on intisalise a la premiere vague
    # ajouter un au numéro de la vague
    NouvelleVague = {vague + 1}
    return NouvelleVague


def spawnMonstre():
    MonstreChoisi = list(ennemis_col.aggregate([{"$sample": {"size": 1}}]))
    return MonstreChoisi[0]  # on ddit qu'on veu le premier dircectement


VagueCombat()
