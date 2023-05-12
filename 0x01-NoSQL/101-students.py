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
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'scores': 1,
                'averageScore': {'$avg': '$scores.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    cur = mongo_collection.aggregate(pipeline)
    return [document for document in cur]
