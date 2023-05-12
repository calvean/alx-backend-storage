#!/usr/bin/env python3
""" Log stats """

from pymongo import MongoClient

if __name__ == "__main__":
    """ check all elements in collection """
    client = MongoClient('mongodb://localhost:27017/')
    collection = client['logs']['nginx']

    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")

    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in http_methods:
        count = collection.count_documents({'method': method})
        print(f"\t{count} {method} requests")

    count = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{count} requests with method=GET and path=/status")
