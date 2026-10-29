#Systeme de combat

#Une fonction pour sélectionné un mostre aléatoirement depuis la bdd 
#Sélectionné un monstre aléatoirement depuis la base de données avec ses caractéristiques 

#Fonction generer_mosntres
#  {on recuere les monstres dans la bdd }

#Fonction monstres_aleatoire()
# prends un monstre au hasard dans generer_monstres 





#Fonction combat_equipe()
  #monstres_aleatoire()
  #cree_equipe()
#tant que la somme des  hp des heros>0 
#fonction attaque(){si pv>O On prend successivement les stat d'attaque des hero qu'on stocke au préalable dans un tableau. on prends la def du monstre et on parcours le tableau en faisant a chaque fois une difference }
#si 


#on prend la valeur d'attaque du hero pour attaquer les pv du monstres 




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














  


    




