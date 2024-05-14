#!/usr/bin/env python3
"""module with a function that inserts a document in a collection
based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """insert document into a collection based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
