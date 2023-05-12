#!/usr/bin/env python3
""" Caching HTTP Requests """

import requests
from functools import wraps
from typing import Callable
import redis


def count_requests(method: Callable):
    """ Count the number of requests to a URL """
    r = redis.Redis()

    @wraps(method)
    def wrapped(url):
        """ Decorated function to count and cache requests """
        r.incr(f"request_count:{url}")
        cached = r.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        response = method(url)
        r.setex(f"cached:{url}", 10, response)
        return response

    return wrapped


@count_requests
def fetch_page(url: str) -> str:
    """ Function to fetch HTML content of a URL """
    return requests.get(url).text
