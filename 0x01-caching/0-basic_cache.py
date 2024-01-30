#!/usr/bin/env python3
"""
Basic Caching Dictionary
"""
from base_caching import BaseCaching


class BasicCache():
    """ A basic caching system
    - You must use self.cache_data - dictionary from parent class BaseCaching
    - This caching system doesn’t have limit
    - def put(self, key, item):
        ~ Must assign to dict self.cache_data the item value 4 key key
        ~ If key or item is None, this method should not do anything.
    - def get(self, key):
        ~ Must return the value in self.cache_data linked to key
        ~ If key is None / doesn’t exist in self.cache_data, return None
    """
    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from cache by key """
        self.cache_data = key

        if key is not None:
            return self.cache_data.get(key, None)
        else:
            return None
