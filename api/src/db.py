import pymongo


client = pymongo.MongoClient("mongodb+srv://Aldo:98WgdtkbH7dlxDys@cluster0.hk31r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('Hack')

records = db.Fraude

print(records.count_documents({}))