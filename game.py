#Systeme de combat

#Une fonction pour sélectionné un mostre aléatoirement depuis la bdd 
#Sélectionné un monstre aléatoirement depuis la base de données avec ses caractéristiques 

#Fonction generer_mosntres {on recuere les monstres dans la bdd }

#Fonction monstres_aleatoire()prends un monstre au hasard dans generer_monstres 
#recuperer les monstres depuis la bdd 
#afficher les monstres successivemem t de maniere aléatoire 
#Renvoyer de

#une nouvelle fonction pour afficher les trois perso choisis par l'utilisateur 
# la fonction de choix aléatoire du monstre est appellé 
#chaque perso de l'équipe attaque le monstre avec 



from db_init import db
import random

def generer_monstres():
     lot_monstres = list(db["Monstre"].find())
     return lot_monstres


def monstre_aleatoire():
    lot_monstres=generer_monstres()
    monstre_selectionne=random.choice(lot_monstres)
    print("++++++Monstres aléatoire+++++++")
    print(f"Nom:{monstre_selectionne.get('name')}")
    print(f"Nom:{monstre_selectionne.get('attack')}")
    print(f"Nom:{monstre_selectionne.get('defense')}")
    print(f"Nom:{monstre_selectionne.get('hp')}")











  


    




