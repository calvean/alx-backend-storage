#!/usr/bin/env python3
""" List documents """
from pymongo.collection import Collection
from typing import List

def list_all(mongo_collection: Collection) -> List[dict]:
    """
    Lists all documents in a MongoDB collection.
    
    Args:
        mongo_collection (Collection): MongoDB collection
    Returns:
        A list of all documents in the collection
    """
    cur = mongo_collection.find({})
    documents = [document for document in cur]

    return documents
