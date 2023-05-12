#!/usr/bin/env python3
""" String Redis """

import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable = None):
    """ count calls """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper method """
        with self._redis.pipeline() as pipe:
            name = method.__qualname__
            pipe.incr(name)
            pipe.execute()

        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable):
    """ Call history """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wraper function """
        with self._redis.pipeline() as pipe:
            inputs = str(args)
            pipe.rpush(method.__qualname__ + ":inputs", inputs)

            output = str(method(self, *args, **kwargs))
            pipe.rpush(method.__qualname__ + ":outputs", output)

            pipe.execute()

        return output

    return wrapper


def replay(func: Callable):
    """ Replay function """
    r = redis.Redis()
    func_name = func.__qualname__
    number_calls = r.get(func_name)

    if number_calls:
        number_calls = int(number_calls.decode('utf-8'))
    else:
        number_calls = 0

    print(f'{func_name} was called {number_calls} times:')

    inputs = r.lrange(func_name + ":inputs", 0, -1)
    outputs = r.lrange(func_name + ":outputs", 0, -1)
    inputs = [i.decode('utf-8') for i in inputs]
    outputs = [o.decode('utf-8') for o in outputs]

    for inp, out in zip(inputs, outputs):
        print(f'{func_name}({inp}) -> {out}')


class Cache:
    """ Functionality Redis """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store Cache
        Args:
            data: information to store
        Return:
            Key or number uuid
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(
      self,
      key: str,
      fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Get the cache
        Args:
            Callable
        Return:
            Cache
        """
        value = self._redis.get(key)

        if fn:
            value = fn(value)

        return value
