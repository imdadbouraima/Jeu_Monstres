#Connection a la base de donneés

import sys
from mongopy import Mongo

def get_database():
    Client=MongoClient("")
    db=Client[""]
    return db
