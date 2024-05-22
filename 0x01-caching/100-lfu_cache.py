#!/usr/bin/env python3
# Task 5: Implementation of a LFU (Least Frequently Used) caching system

from collections import OrderedDict
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    # LFUCache is a class that inherits from BaseCaching and implements a LFU caching system

    def __init__(self):
        # Initializes the cache as an ordered dictionary to maintain the order of insertion
        # Also initializes a list to keep track of the frequency of each key
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        # The __reorder_items method reorders the items in the cache based on the most recently used item
        # It updates the frequency of the most recently used key and reorders the keys_freq list accordingly

        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        # The put method stores the item with a given key in the cache_data dictionary
        # It only stores the item if both the key and item are not None
        # If the cache is full (i.e., has more items than MAX_ITEMS), it removes the least frequently used item before storing the new one

        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        # The get method retrieves the value associated with a given key from the cache_data dictionary
        # If the key is not found in the dictionary, it returns None
        # If the key is found, it updates the frequency of the key and reorders the keys_freq list

        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
