#!/usr/bin/env python3
""" String Redis """

import requests
import redis
from functools import wraps


redis_client = redis.Redis()

def cache_decorator(expires):
    """Cache decorator to store function results in Redis"""

    def decorator(func):
        """ Decorator Function """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """ Wrapper Function """
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            result = redis_client.get(cache_key)
            if result is not None:
                return result.decode("utf-8")

            result = func(*args, **kwargs)
            redis_client.setex(cache_key, expires, result)

            return result

        return wrapper

    return decorator

@cache_decorator(expires=10)
def get_page(url):
    """Fetches HTML content of given URL and caches the result"""

    redis_client.incr(f"count:{url}")
    response = requests.get(url)
    return response.content.decode("utf-8")

