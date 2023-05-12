#!/usr/bin/env python3
""" stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    logs_col = client.logs.nginx

    x = logs_col.count_documents({})
    print(f"{x} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_col.count_documents({"method": method})
        print(f"method {method}: {count}")

    count = logs_col.count_documents({"method": "GET", "path": "/status"})
    print(f"{count} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    for doc in logs_col.aggregate(pipeline):
        print(f"    {doc['_id']}: {doc['count']}")
