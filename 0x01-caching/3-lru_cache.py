#!/usr/bin/env python3
"""
This module contains the LRUCache class which inherits from BaseCaching
and is a caching system following the Least Recently Used (LRU) algorithm.
"""

from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """
    A LRUCache class that inherits from BaseCaching and is a caching system.
    This caching system follows the Least Recently Used (LRU) algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        you must discard the least recently used item (LRU algorithm)
        you must print DISCARD: with the key discarded and following by a new line
        """
        if key is not None and item is not None:
            if key in self.keys:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discarded_key = self.keys.popleft()
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        if key is not None and key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key, None)
