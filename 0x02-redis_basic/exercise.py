#!/usr/bin/env python3
"""redis storage module to implement redis storage"""
import uuid
import redis
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable) -> Callable:
        """accepts key and a callable as argument and returns
        the value of that key from a redis database"""
        value = self._redis.get(key)
        if fn is None:
            return value
        else:
            return fn(value)

    def get_str(self, key: str) -> str:
        """parameterizes get methon with the callable to convert
        return value to byte string
        """
        return self.get(key, lambda v: v.decode('utf-8'))

    def get_int(self, key: int) -> int:
        """parameterize get method with the callable to convert
        return value int
        """
        return self.get(key, lambda n: int(n))
