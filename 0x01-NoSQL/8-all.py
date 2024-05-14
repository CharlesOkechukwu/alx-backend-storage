#!/usr/bin/env python3
"""list all documents in a collection module"""
from pymongo import MongoClient
from typing import Iterator


def list_all(mongo_collection: MongoClient) -> Iterator:
    """list all documents in a collection"""
    return [document for document in mongo_collection.find()]
