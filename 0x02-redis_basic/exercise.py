#!/usr/bin/env python3
"""redis storage module to implement redis storage"""
import uuid
import redis
from typing import Union


class Cache:
    """redis class to store an instance of redis client"""
    def __init__(self):
        """initialize class attributes"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a key using uuid to store data in redis
        and return key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
