import os
from parser import parser
from collections import defaultdict
import pymongo
from pymongo import UpdateOne
import json

# my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
# mydb = my_client["searchData"]
# mycol = mydb["test"]

root = 'WEBPAGES_RAW'
pnum = 0
raw = dict()
p = "p"
operations = list()
wordcount = defaultdict()
#mycol.create_index([("token",pymongo.HASHED)])

for subdir, dirs, files in os.walk(root):
    for f in files:
        if not f.endswith('.json') and not f.endswith('.tsv') and not f.endswith('.DS_Store'):
            dir_path = os.path.join(subdir,f)
            raw = parser(dir_path)
            doc_id = dir_path.replace('WEBPAGES_RAW/', '')
            wordcount[doc_id] = 0
            for term, freq in raw.items():
                wordcount[doc_id] += (freq)
    #             p += str(pnum)
    #             operations.append(UpdateOne({"token":term}, {"$set": {p: {"doc": doc_id, "freq": freq}}}, upsert=True))
    #             r = ''.join([i for i in p if not i.isdigit()])
    #             p = r
    #             pnum += 1
    # if len(operations) != 0:
    #     mycol.bulk_write(operations)
    #     operations.clear()

with open('word_count.json', 'w') as outfile:
    json.dump(wordcount, outfile)

