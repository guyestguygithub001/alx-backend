#!/usr/bin/env python3
# Task 3: Implementation of a LRU (Least Recently Used) caching system

from collections import OrderedDict
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    # LRUCache is a class that inherits from BaseCaching and implements a LRU caching system

    def __init__(self):
        # Initializes the cache as an ordered dictionary to maintain the order of insertion
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        # The put method stores the item with a given key in the cache_data dictionary
        # It only stores the item if both the key and item are not None
        # If the cache is full (i.e., has more items than MAX_ITEMS), it removes the least recently used item before storing the new one

        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        # The get method retrieves the value associated with a given key from the cache_data dictionary
        # If the key is not found in the dictionary, it returns None
        # If the key is found, it moves the key to the end of the dictionary to mark it as recently used

        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
