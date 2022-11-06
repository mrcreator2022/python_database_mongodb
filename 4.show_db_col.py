import collections
import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    #database list
    allDatabases = client.list_database_names()
    print(allDatabases)

    #collection show
    col = client['pythondb']
    print(col.list_collection_names())
    