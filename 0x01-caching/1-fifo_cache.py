#!/usr/bin/env python3
""" FIFO Caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """  Inherits from BaseCaching and is a caching system
    - Overload def __init__(self): but don’t forget 2 call parent init:
            super().__init__()
    - def put(self, key, item):
         ~ Must assign to dict self.cache_data the item value for the key key
         ~ If key or item is None, this method should not do anything.
         ~ If number of items in self.cache_data is higher BaseCaching.MAX_ITEM
            * discard the first item put in cache (FIFO algorithm)
            * print DISCARD: with key discarded and following by a new line
    - def get(self, key):
          ~ return the value in self.cache_data linked to key
          ~ If key is None / doesn’t exist in self.cache_data, return None
    """
    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add an item to cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard 1st item (FIFO)
                discarded_key = next(iter(self.cache_data))
                self.cache_data.pop(discarded_key)
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item

    def get(self, key):
        """ Gets items fron Cache """
        if key is not None:
            return self.cache_data.get(key, None)
