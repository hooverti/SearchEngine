import pymongo

my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
mydb = my_client["search_index"]
mycol = mydb["tokens"]


term = input("Search: ")
print("You searched for: ", term)
for i in mycol.find({"token": term}, {"page": 1, "freq": 0, "_id": 0}):
    print(i)
