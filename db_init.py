#Connection a la base de donneés


from pymongo import MongoClient

def get_database():
    Client=MongoClient("mongodb://localhost:27017/")
    db=Client["Jeu_video"]
    return db
db = get_database()


