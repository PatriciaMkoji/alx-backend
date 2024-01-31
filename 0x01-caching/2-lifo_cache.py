#!/usr/bin/env python3
""" Implement LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO classthat inherits from BaseCaching

    Attributes:
        MAX_ITEMS: Max number

    Methods:
        __init__: Initializes the FIFOCache
        put: Adds ands item to the cache
        get: Retrieves an item from the cache
    """
    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add items in the Cache """
        if key is not None or item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard last item (LIFO)
                discarded_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(discarded_key)
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item

    def get(self, key):
        """ Get items from Cache """
        if key is not None:
            return self.cache_data.get(key, None)
