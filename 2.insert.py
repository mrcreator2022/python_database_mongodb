import collections
import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['pythondb']
    collection = db['students']

    #Insert one
    # dictionary = {'name':'veer','marks':50}
    # collection.insert_one(dictionary)

    # dictionary2 = {'name':'ram','marks':70}
    # collection.insert_one(dictionary2)

    #Insert many
    insertThese = [
        {'name':'Veer','location':'Delhi','marks':34},
        {'name':'Veer','location':'Delhi','marks':94},
        {'name':'Sunil','location':'Ujjain','marks':44},
        {'name':'Kamal','location':'Indore','marks':54},
        {'name':'Komal','location':'Khandwa','marks':64}
    ]

    collection.insert_many(insertThese)
