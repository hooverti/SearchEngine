import pymongo
import json
from collections import defaultdict

def search(term):
    my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
    mydb = my_client["searchData"]
    mycol = mydb["tokens"]

    with open("WEBPAGES_RAW/bookkeeping.json") as handle:
        jsonDict = json.loads(handle.read())
    test_list = dict()
    urlDict = defaultdict()
    while True:
        for i in mycol.find({"token": term}, {"_id": 0, "token": 0}):
            test_list = i

        docID = list()

        #this is a stupid way to do this, let's make it better later
        for x in test_list.values():
            for items in x.values():
                if type(items) == str:
                    docID.append(items)

        test_list.clear()

        for doc in docID:
            urlDict[doc] = jsonDict[doc]

        docID.clear()
        return urlDict
