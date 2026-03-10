from db_init import equipe_col, ennemis_col
import random


def spawnMonstre():
    MonstreChoisi = list(ennemis_col.aggregate([{"$sample": {"size": 1}}]))
    return MonstreChoisi[0]


def test():
    monstre = spawnMonstre()
    monstreNom = monstremonstre = spawnMonstre()

    # Pour avoir une valeur précise :
    nom = monstre["nom"]
    print(f"le monster slectionné ets {nom} ")


test()
