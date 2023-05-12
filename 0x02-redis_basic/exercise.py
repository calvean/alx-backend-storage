#!/usr/bin/env python3
""" String Redis """

import uuid
import redis


class Cache:
    """ Functionality Class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store Cache
        Args:
            data: information to store
        Return:
            Key or number uuid
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
