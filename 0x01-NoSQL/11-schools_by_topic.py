#!/usr/bin/env python3
""" list of schools """

from typing import List
import pymongo


def schools_by_topic(mongo_collection, topic: str) -> List[str]:

    result = mongo_collection.find({'topics': topic})

    return [doc['name'] for doc in result]
