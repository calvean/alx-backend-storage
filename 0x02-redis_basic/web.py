#!/usr/bin/env python3
""" Redis Caching Decorator """

import requests
import redis
from functools import wraps

redis_client = redis.Redis()


def cache_decorator(expires: int, redis_client: redis.Redis):
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


redis_cache = cache_decorator(expires=10, redis_client=redis_client)


@redis_cache
def get_page(url: str) -> str:
    """Fetches HTML content of given URL and caches the result"""

    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.exceptions.RequestException, ValueError):
        return ''

    redis_client.incr(f"count:{url}")
    return response.content.decode("utf-8")
