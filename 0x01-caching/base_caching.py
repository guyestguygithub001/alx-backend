#!/usr/bin/python3
# BaseCaching module

class BaseCaching():
    # The BaseCaching class defines the basic structure and operations of a caching system
    # It includes the constants of the caching system and the storage structure (a dictionary)

    MAX_ITEMS = 4  # Maximum number of items that can be stored in the cache

    def __init__(self):
        # Initializes the cache by creating an empty dictionary to store the data
        self.cache_data = {}

    def print_cache(self):
        # The print_cache method displays the current state of the cache
        # It prints each key-value pair stored in the cache
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        # The put method is intended to add an item to the cache
        # It needs to be implemented in any class that inherits from BaseCaching
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        # The get method is intended to retrieve an item from the cache by its key
        # It needs to be implemented in any class that inherits from BaseCaching
        raise NotImplementedError("get must be implemented in your cache class")
