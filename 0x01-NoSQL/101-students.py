#!/usr/bin/env python3
""" list of schools """

import pymongo


def top_students(mongo_collection):
    """
    function that returns all students sorted by average score
    Args:
        mongo_collection: MongoDB Collection

    Return:
        all students sorted by average score
    """
    cur = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return cur
