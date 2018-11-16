import pymongo

my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
mydb = my_client["search_index"]
mycol = mydb["tokens"]


term = input("Search: ")
print("Looking that info up for you...")
for i in mycol.find({"token": term}, {"token": 0, "freq": 0, "_id": 0}):
    print(i)
