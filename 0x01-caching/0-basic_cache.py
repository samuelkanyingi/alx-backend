#!/usr/bin/env python3
""" BaseCaching module
"""


from base_caching import BaseCaching
class BasicCache(BaseCaching):
    """BaseCaching defines:
      - a dictionary `cache_data`
    """

    def __init__(self):
        """Init the class
        """
        self.cache_data = {}

    def print_cache(self):
        """Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data[key]))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
