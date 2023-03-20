from pymongo import MongoClient

#Base de datos local
#db_client= MongoClient(host="localhost").local

#Base de datos Remota
db_client = MongoClient("mongodb+srv://test:test@cluster0.r8fqclo.mongodb.net/?retryWrites=true&w=majority").test