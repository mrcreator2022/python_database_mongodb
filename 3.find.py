import collections
import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['pythondb']
    collection = db['students']
    
    #find one
    # one = collection.find_one({'name':'Meet'})
    # print(one)

    allDocs = collection.find({'name':"Veer"})
    #allDocs = collection.find({'name':'veer'})
    #allDocs = collection.find({'name':'veer'},{'name':1,'_id':0})
    # allDocs = collection.find({'name':'ram'},{'name':1,'_id':0})
    #allDocs = collection.find({'name':'veer'},{'name':1,'_id':0}).limit(1)
    # allDocs = collection.find({"name":"Veer","Marks":{"$lte":80}})
    # print(collection.count_documents({}))
    for item in allDocs:
        item['student_id'] = item['_id']
        print(item)
    # print(allDocs)
