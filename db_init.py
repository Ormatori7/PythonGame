#  python .\db_init.py pour initialiser la base de donnée
# mongodb://localhost:27017/ a ouvrir dans le navigateur pour voir la base de donnée dans MongoDB Compass

# On importe MongoClient, le "chauffeur" qui fait le trajet entre ton code et le serveur MongoDB
from pymongo import MongoClient

# 1. CONNEXION AU SERVEUR
# On se connecte au serveur qui tourne sur ton propre ordinateur (localhost) sur le port 27017
client = MongoClient("localhost", 27017)

# 2. ACCÈS À LA BASE DE DONNÉES
# On accède à (ou on crée) la base de données nommée "game_db"
db = client["game_db"]


# 3. DÉFINITION DES COLLECTIONS (LES "TI=ROIRS")
# On crée des variables pour pointer vers nos collections.
# Intérêt : si tu changes le nom "characters" ici, il est mis à jour partout dans ton script
personnages_col = db.characters
ennemis_col = db.enemy
classement_col = db.classement
equipe_col = db.equipe


def init_database():

    # 4. NETTOYAGE (RESET)
    # On vide les tiroirs avant de les remplir pour éviter d'avoir 20 chevaliers si on lance le script 2 fois
    # Le dictionnaire vide {} signifie "supprime TOUT sans condition"
    personnages_col.delete_many({})
    ennemis_col.delete_many({})
    equipe_col.delete_many({})

    # 5. PRÉPARATION DES DONNÉES
    # On utilise des listes de dictionnaires {}. C'est le format "Document" que MongoDB adore
    ListeCharacter = [
        {"id_ref": "1", "nom": "Prince", "atk": 15, "def": 10, "hp": 100},
        {"id_ref": "2", "nom": "sorcier", "atk": 15, "def": 20, "hp": 75},
        {"id_ref": "3", "nom": "archer", "atk": 20, "def": 5, "hp": 90},
        {"id_ref": "4", "nom": "bouclier", "atk": 15, "def": 0, "hp": 120},
        {"id_ref": "5", "nom": "PoidLourd", "atk": 15, "def": 10, "hp": 150},
        {"id_ref": "6", "nom": "Assasin", "atk": 50, "def": 15, "hp": 80},
        {"id_ref": "7", "nom": "Russe", "atk": 25, "def": 5, "hp": 200},
        {"id_ref": "8", "nom": "Roi", "atk": 15, "def": 8, "hp": 200},
        {"id_ref": "9", "nom": "Fou", "atk": 90, "def": 5, "hp": 25},
        {"id_ref": "10", "nom": "Paysan", "atk": 15, "def": 5, "hp": 50},
    ]

    ListeEnemy = [
        {"nom": "le robot", "atk": 10, "def": 5, "hp": 100},
        {"nom": "le fantome", "atk": 15, "def": 15, "hp": 120},
        {"nom": "le chevalier de l'apocalypse", "atk": 20, "def": 10, "hp": 150},
        {"nom": "le zombie", "atk": 10, "def": 10, "hp": 100},
        {"nom": "le Dragon", "atk": 25, "def": 7, "hp": 130},
        {"nom": "Le mime", "atk": 25, "def": 8, "hp": 150},
    ]

    # 6. INSERTION DANS LA BASE
    # On range nos listes Python dans les tiroirs MongoDB correspondants
    # .insert_many() envoie toute la liste d'un coup, c'est très performant
    personnages_col.insert_many(ListeCharacter)
    ennemis_col.insert_many(ListeEnemy)

    # 7. CONFIRMATION VISUELLE
    # On affiche un petit message dans la console pour savoir que tout s'est bien passé
    print("✓ Base de données initialisée avec succès !")
    print(f"  - {len(ListeCharacter)} personnages ajoutés")
    print(f"  - {len(ListeEnemy)} ennemis ajoutés")

    # 8. FERMETURE
    # On ferme la porte du serveur proprement pour libérer de la mémoire sur ton PC
    # client.close()


# 9. DÉCLENCHEMENT DU SCRIPT
# Cette condition vérifie si on a cliqué sur "Play" sur ce fichier précis.
# Si oui, on lance la fonction init_database()
if __name__ == "__main__":
    init_database()
