import os
from parser import parser
from collections import defaultdict
import pymongo


my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
mydb = my_client["searchData"]
mycol = mydb["tokens"]


#def create_corpus():
root = 'WEBPAGES_RAW/1'
word_dict = defaultdict(list)
pnum = 0
p = "p"
for subdir, dirs, files in os.walk(root):
    for f in files:
        dir_path = os.path.join(subdir,f)
        raw = parser(dir_path)
        doc_id = dir_path.replace('WEBPAGES_RAW/', '')
        for term, freq in raw.items():
            p += str(pnum)
            mycol.update({"token":term}, {"$set": {p: {"doc": doc_id, "freq": freq}}}, True)
            r = ''.join([i for i in p if not i.isdigit()])
            p = r
            pnum += 1




# mycol.insert_one(
#     {"token": "vision",
#      "p1": {"doc":"1/12","freq":"3"},
#      "p2": {"doc": "1/34", "freq":"1"}
#      })
# print("done")
# mycol.insert_one(
#     {"token": "california",
#      "p1": {"doc":"1/1","freq":"7"},
#      "p2": {"doc": "1/9", "freq":"2"}
#      })
# print("done2")
# mycol.insert_one(
#     {"token": "october",
#      "p1": {"doc":"1/45","freq":"9"},
#      "p2": {"doc": "1/100", "freq":"4"}
#      })
# print('all done')

#mycol.update({"token":"vision"},{"$set": {"p3":{"doc":"1/33","freq":"2"}}})

# for x in mycol.find():
#     print(x)
