#!/usr/bin/env python3
"""module to define a function that returns list of schools
with a topic"""


def schools_by_topic(mongo_collection, topic):
    """returns list of schools with a specific topic"""
    return mongo_collection.find({'topics': topic})
