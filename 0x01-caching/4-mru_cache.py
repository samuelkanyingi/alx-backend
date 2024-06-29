#!/usr/bin/python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a caching system with MRU eviction policy """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
