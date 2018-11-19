import os
from parser import parser
import pymongo


my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
mydb = my_client["searchData"]
mycol = mydb["tokens"]

root = 'WEBPAGES_RAW'
pnum = 0
p = "p"

for subdir, dirs, files in os.walk(root):
    for f in files:
        if not f.endswith('.json') and not f.endswith('.tsv'):
            dir_path = os.path.join(subdir,f)
            raw = parser(dir_path)
            doc_id = dir_path.replace('WEBPAGES_RAW/', '')
            print(doc_id)
            for term, freq in raw.items():
                p += str(pnum)
                mycol.update({"token":term}, {"$set": {p: {"doc": doc_id, "freq": freq}}}, True)
                r = ''.join([i for i in p if not i.isdigit()])
                p = r
                pnum += 1

