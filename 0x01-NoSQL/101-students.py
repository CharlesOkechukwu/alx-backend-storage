#!/usr/bin/env python3
"""list all students sorted by average score"""


def top_students(mongo_collection):
    """return all students sorted by average score"""
    students = mongo_collection.aggregate([
        {'$addFields': {'averageScore': {'$avg': "$topics.score"}}},
        {'$sort': {'averageScore': -1}}
    ])
    return students
