#!/usr/bin/env python3
"""module that defines a function to update document in
a collection"""


def update_topics(mongo_collection, name, topics):
    """update all topics of all document of a collection by name"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
