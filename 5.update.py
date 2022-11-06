import collections
import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['pythondb']
    collection = db['students']
    
    pre = {"name": "veer"}
    nextt = {"$set": {"location": "Indore"}}

    #Update One
    #collection.update_one(pre,nextt)

    #Update Many
    collection.update_many(pre,nextt)

    #check modified count
    # up = collection.update_many(pre,nextt)
    # print(up.modified_count)    
