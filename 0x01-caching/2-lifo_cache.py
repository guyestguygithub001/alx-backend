#!/usr/bin/env python3
"""
This module contains the LIFOCache class which inherits from BaseCaching
and is a caching system following the Last In, First Out (LIFO) algorithm.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A LIFOCache class that inherits from BaseCaching and is a caching system.
    This caching system follows the Last In, First Out (LIFO) algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        you must print DISCARD: with the key discarded and following by a new line
        """
        if key is not None and item is not None:
            if key in self.keys:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discarded_key = self.keys.pop()
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
