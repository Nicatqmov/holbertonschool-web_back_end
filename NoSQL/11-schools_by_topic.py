#!/usr/bin/env python3
'''Python function that insert school in a collection
'''

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
        """
    Insert a new document in a collection based on kwargs.

    :param mongo_collection: The pymongo collection object
    :param kwargs: The fields and values to insert in the new document
    :return: The new _id of the inserted document
    """
    schools = mongo_collection.find('topic' : topic)

    return schools