import pymongo
client = pymongo.MongoClient("mongodb+srv://Gourangpatidar:8839006621@cluster0.fqipgtj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    "name":"gourang" ,
    "surname":"patidar"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)