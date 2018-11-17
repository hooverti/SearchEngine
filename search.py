import pymongo

my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
mydb = my_client["searchData"]
mycol = mydb["tokens"]

test_list = dict()
term = input("Search: ")
print("Looking that info up for you...")

for i in mycol.find({"token": term}, {"_id": 0, "token": 0}):
    test_list = i

docID = list()
urlList = list()

#this is a stupid way to do this, let's make it better later
for x in test_list.values():
    for items in x.values():
        if type(items) == str:
            docID.append(items)

