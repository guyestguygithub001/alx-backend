#!/usr/bin/env python3
"""
This module contains the FIFOCache class which inherits from BaseCaching
and is a caching system following the First In, First Out (FIFO) algorithm.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFOCache class that inherits from BaseCaching and is a caching system.
    This caching system follows the First In, First Out (FIFO) algorithm.
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
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded and following by a new line
        """
        if key is not None and item is not None:
            if key not in self.keys:
                if len(self.keys) >= self.MAX_ITEMS:
                    discarded_key = self.keys.pop(0)
                    del self.cache_data[discarded_key]
                    print('DISCARD: {}'.format(discarded_key))
                self.keys.append(key)
            else:
                self.keys.remove(key)
                self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
