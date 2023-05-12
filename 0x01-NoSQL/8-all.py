#!/usr/bin/env python3
""" List documents """

import pymongo


def list_all(mongo_collection) -> list:
    """
    Lists all documents in a MongoDB collection.
    Args:
        mongo_collection (Collection): MongoDB collection
    Returns:
        A list of all documents in the collection
    """
    cur: list = []

    for document in mongo_collection.find():
        cur.append(document)

    return cur
