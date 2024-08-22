#!/usr/bin/env python3
'''Python function that insert school in a collection
'''
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
     """
    Insert a new document in a collection based on kwargs.

    :param mongo_collection: The pymongo collection object
    :param kwargs: The fields and values to insert in the new document
    :return: The new _id of the inserted document
    """

    mongo_collection.update(
        {'name' : name},
        {'$set' : {'topics' : topics}}
        )

