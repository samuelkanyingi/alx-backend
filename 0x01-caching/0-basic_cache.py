#!/usr/bin/env python3
""" BaseCaching module
"""


class BaseCaching():
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
