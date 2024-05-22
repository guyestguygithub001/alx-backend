#!/usr/bin/env python3

# Task 1: Implementation of a FIFO (First In, First Out) caching system

from collections import OrderedDict
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    # FIFOCache is a class that inherits from BaseCaching and implements a FIFO caching system

    def __init__(self):
        super().__init__()
        # Initialize the cache_data dictionary as an ordered dictionary to maintain the order of insertion
        self.cache_data = OrderedDict()

    def put(self, key, item):
        # The put method stores the item with a given key in the cache_data dictionary
        # It only stores the item if both the key and item are not None
        # If the cache is full (i.e., has more items than MAX_ITEMS), it removes the oldest item before storing the new one

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        # The get method retrieves the value associated with a given key from the cache_data dictionary
        # If the key is not found in the dictionary, it returns None

        return self.cache_data.get(key, None)

