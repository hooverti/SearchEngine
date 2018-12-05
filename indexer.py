import os
from parser import parser
from collections import defaultdict
import pymongo
from pymongo import UpdateOne
import json

# connect to MongoDB
my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
mydb = my_client["searchData"]
mycol = mydb["test"]

root = 'WEBPAGES_RAW'
pnum = 0
raw = dict()
p = "p"
operations = list()
wordcount = defaultdict()
# create a hashed index on tokens in our DB
mycol.create_index([("token",pymongo.HASHED)])

# walk through the WEBPAGES_RAW folder and add the words from those files to our DB
for subdir, dirs, files in os.walk(root):
    for f in files:
        # avoid the json, tsv, and apple files in the folder
        if not f.endswith('.json') and not f.endswith('.tsv') and not f.endswith('.DS_Store'):
            dir_path = os.path.join(subdir,f)
            # call our parser to parse the page
            raw = parser(dir_path)
            # remove WEBPAGES_RAW so we can get the doc-id
            doc_id = dir_path.replace('WEBPAGES_RAW/', '')
            wordcount[doc_id] = 0
            for term, freq in raw.items():
                # add all the term frequencies for each document so we can get the total number of words in each document
                wordcount[doc_id] += (freq)
                # build and destroy p# to create new and unique postings for the DB
                p += str(pnum)
                # update with upsert on every term found in every document (create new if doesn't exist else update postings list)
                operations.append(UpdateOne({"token":term}, {"$set": {p: {"doc": doc_id, "freq": freq}}}, upsert=True))
                r = ''.join([i for i in p if not i.isdigit()])
                p = r
                pnum += 1
    # we use bulk_write here to vastly improve DB build time
    if len(operations) != 0:
        mycol.bulk_write(operations)
        operations.clear()
# write the total word count to the json file for later
with open('word_count.json', 'w') as outfile:
    json.dump(wordcount, outfile)

