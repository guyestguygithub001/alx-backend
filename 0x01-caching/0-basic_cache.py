#!/usr/bin/env python3

# Task 0: Implementation of a basic dictionary

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    # BasicCache is a class that inherits from BaseCaching and implements a basic caching system

    def put(self, key, item):
        # The put method stores the item with a given key in the cache_data dictionary
        # It only stores the item if both the key and item are not None
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        # The get method retrieves the value associated with a given key from the cache_data dictionary
        # If the key is not found in the dictionary, it returns None

        return self.cache_data.get(key, None)

