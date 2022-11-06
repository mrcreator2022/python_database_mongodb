import collections
import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['pythondb']
    collection = db['students']
    
    rec = {"name": "Meet"}
    #Delete One
    collection.delete_one(rec)

    #Delete Many
    #collection.delete_many(rec)
    
    #count delete record
    # up = collection.delete_many(rec)
    # print(up.deleted_count)
   
