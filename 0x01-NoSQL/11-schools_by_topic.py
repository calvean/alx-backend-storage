#!/usr/bin/env python3
""" list of schools """

from typing import List
import pymongo


def schools_by_topic(mongo_collection, topic: str) -> List[str]:
    """
    function that changes all topics of a school document based on the name
    Args:
        mongo_collection: MongoDB Collection
        name: school name to update
        topics: list of topics approached in the school

    Return:
        number of updated documents
    """
    results: list = []

    for result in mongo_collection.find({'topics': topic}):
        results.append(result)

    return results
