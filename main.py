#Proposer un menu a l'utilisateur 
#{Le menu doit comporter:une option pour 
#1-Demarrer le jeu 
#2-Afficher le classement
#3-Quitter}

#Contrainte:Si l'utilisateur entre un autre nombre que {1 2 3 }OU meme une lettre on  renvoie une erreur 

#Si 1(Démarrer le jeu ) alors on propose un affichage pour 
#{a-Choix nom utilisateur 
#Le choix du nom utilisateur est obligatoire }

#b-Création d'équipe


#une fois le nom de l'utilisateur entrée  l'utilisateur doit créer son équipe on propose un menu pour la création de l'équipe


# Menu creation d'équipe 
# Affichage des différents heros disponibles avec leur points disponibles en suivant 
# ce format pour permettre a l'utilisateur de choisir son personnage

#Chaque personnage peut etre sélectionner une seul fois 
# 1-Personnage 1- ATK X1,DEF Y1,PV Z1;
# 2-personnage 2-ATK X2,DEF Y2,PV Z2;
# 3-personnage 3-ATK X3,DEF Y3,PV Z3;
# 4-personnage 4-ATK X4,DEF Y4,PV Z4;
# 5-personnage 5-ATK X5,DEF Y5,PV Z5;
# 6-personnage 6-ATK X6,DEF Y6,PV Z6;
# 7-personnage 7-ATK X7,DEF Y7,PV Z7;
# 8-personnage 8-ATK X8,DEF Y8,PV Z8;
# 9-personnage 9-ATK X9,DEF Y9,PV Z9;


#Choix des personnages 
#Si 1 on affiche personnage 1,si deux on affiche personnage 2,si 3 on affiche personnage 3  
#On affiche le nom de tous les personnages que l'utilisateur aura choisis DANS equipe 

#Equipe:Personnage1,Personnage2,Personnage3


def main():
    db=get_database



