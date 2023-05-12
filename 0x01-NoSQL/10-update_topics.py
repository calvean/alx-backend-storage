#!/usr/bin/env python3
""" Change school topics """

from typing import List
from pymongo.collection import Collection
from pymongo.results import UpdateResult


def update_topics(
  mongo_collection: Collection,
  name: str,
  topics: List[str]) -> int:
    """
    function that changes all topics of a school document based on the name
    Args:
        mongo_collection: MongoDB Collection
        name: school name to update
        topics: list of topics approached in the school

    Return:
        number of updated documents
    """
    result: UpdateResult = mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

    return result.modified_count
