#!/usr/bin/env python3
""" Change school topics """

from typing import List
import pymongo


def update_topics(
  mongo_collection,
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
    mongo_collection.update_many(
      {'name': name},
      {'$set': {'topics': topics}})
