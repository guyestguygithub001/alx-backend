#!/usr/bin/env python3
# Task 2: Implementation of a LIFO (Last In, First Out) caching system

from collections import OrderedDict
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    # LIFOCache is a class that inherits from BaseCaching and implements a LIFO caching system

    def __init__(self):
        # Initializes the cache as an ordered dictionary to maintain the order of insertion
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        # The put method stores the item with a given key in the cache_data dictionary
        # It only stores the item if both the key and item are not None
        # If the cache is full (i.e., has more items than MAX_ITEMS), it removes the most recently added item before storing the new one

        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        # The get method retrieves the value associated with a given key from the cache_data dictionary
        # If the key is not found in the dictionary, it returns None

        return self.cache_data.get(key, None)

