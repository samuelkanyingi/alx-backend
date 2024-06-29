#!/usr/bin/python3
""" LFUCache module """

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache defines a caching system with LFU eviction policy """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.freq = defaultdict(int)  # Frequency of keys
        self.usage = []  # List of (key, frequency) tuples

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.freq[key] += 1
        else:
            self.freq[key] = 1

        self.cache_data[key] = item
        self.usage.append((key, self.freq[key]))

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.evict()

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage.append((key, self.freq[key]))
        return self.cache_data[key]

    def evict(self):
        """ Evict the least frequently used item """
        lfu_keys = sorted(self.usage, key=lambda x: (x[1],
                          self.usage.index(x)))
        lfu_key = lfu_keys[0][0]

        self.usage = [entry for entry in self.usage if entry[0] != lfu_key]
        del self.cache_data[lfu_key]
        del self.freq[lfu_key]
        print("DISCARD:", lfu_key)
