#!/usr/bin/env python3
""" Insert a document in Python  """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: MongoDB Collection
        kwargs: Dictionary with elements
    Return:
        Id of the new element
    """
    c = mongo_collection.insert_one(kwargs)

    return (c.inserted_id)
