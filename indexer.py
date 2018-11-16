import os
from parser import parser
from collections import defaultdict
import pymongo

my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
mydb = my_client["search_index"]
mycol = mydb["tokens"]


def create_corpus():
    root = 'WEBPAGES_RAW/1'
    word_dict = defaultdict(list)

    for subdir, dirs, files in os.walk(root):
        for f in files:
            dir_path = os.path.join(subdir,f)
            raw = parser(dir_path)
            doc_id = dir_path.replace('WEBPAGES_RAW/','')
            for term, freq in raw.items():
                posting = [doc_id, freq]
                if term not in word_dict:
                    word_dict[term].append(posting)
                else:
                    word_dict[term].append(posting)


