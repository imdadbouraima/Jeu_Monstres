#Connection a la base de donneés

import sys 
from mongopy import Mongo

def get_database():
    Client=MongoClient("mongodb://localhost27017")
    db=Client["Jeu_video"]
    return db


