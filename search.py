import pymongo
import json
from collections import defaultdict
import math

def search(term):
    terms = term.split()
    # connect to MongoDB
    my_client = pymongo.MongoClient("mongodb+srv://Rodriguez:0wE*RJ4d^7T6$pIU^tkY@cs121-searchdatabase-vsvf7.mongodb.net/test?retryWrites=true")
    mydb = my_client["searchData"]
    mycol = mydb["tokens"]
    # open our word_count file used for tf-idf
    with open("word_count.json") as wc:
        wcDict = json.loads(wc.read())
    # open the bookkeeping file used to get URL from doc-id
    with open("WEBPAGES_RAW/bookkeeping.json") as handle:
        jsonDict = json.loads(handle.read())

    test_list = dict()
    urlList = list()
    bigList = list()
    urlSet = set()
    while True:
        # iterate through each word in our search query
        for term in terms:
            # search MongoDB for the query and return each posting list
            for i in mycol.find({"token": term}, {"_id": 0, "token": 0}):
                test_list = i
            docID = defaultdict()
            d = None
            wcList = list()
            # if we found something matching the query then calculate idf, get the tf and doc-id, and sort them by tf-idf
            if len(test_list) != 0:
                idf = math.log(len(wcDict)/len(test_list))
                # go through search query results and get the doc-id and the term frequency for that document
                for x in test_list.values():
                    for items in x.values():
                        if type(items) == str:
                            docID[items] = None
                            d = items
                            wcList.append(wcDict[items])
                        if type(items) == int:
                            docID[d] = items

                test_list.clear()
                i = 0
                # calculate the tf-idf score for each result
                for k, v in docID.items():
                    tf = math.log(v/wcList[i])
                    tf_idf = (tf*idf)
                    i += 1
                    docID[k] = tf_idf
                # sort the results by highest tf-idf to lowest tf-idf
                rankedList = list({ k for k,v in sorted(docID.items(), key=lambda x: -x[1]) })

                # find correct URL for the doc-id we found
                for doc in rankedList:
                     urlList.append(jsonDict[doc])

                bigList.append(urlList)

                docID.clear()
        # get the intersection of multiple word searches and pass that intersection to the gui
        if len(bigList) != 0:
            urlSet = set(bigList[0])
            for l in bigList:
                urlSet = urlSet.intersection(l)

        urlList = list(urlSet)
        return urlList
