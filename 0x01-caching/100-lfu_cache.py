#!/usr/bin/env python3
"""
This module contains the LFUCache class which inherits from BaseCaching
and is a caching system following the Least Frequently Used (LFU) algorithm.
"""

from base_caching import BaseCaching
from collections import Counter


class LFUCache(BaseCaching):
    """
    A LFUCache class that inherits from BaseCaching and is a caching system.
    This caching system follows the Least Frequently Used (LFU) algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.keys = []
        self.counts = Counter()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        you must discard the least frequency used item (LFU algorithm)
        if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
        you must print DISCARD: with the key discarded and following by a new line
        """
        if key is not None and item is not None:
            if key in self.keys:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                least_frequent = min(self.counts, key=self.counts.get)
                self.keys.remove(least_frequent)
                del self.cache_data[least_frequent]
                del self.counts[least_frequent]
                print('DISCARD: {}'.format(least_frequent))
            self.keys.append(key)
            self.cache_data[key] = item
            self.counts[key] += 1

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        if key is not None and key in self.keys:
            self.counts[key] += 1
        return self.cache_data.get(key, None)
