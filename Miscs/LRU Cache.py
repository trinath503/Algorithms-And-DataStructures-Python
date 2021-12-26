from collections import OrderedDict

class Cache:

    DEFAULT_CAPACITY = 10 

    def  __init__(self, capacity=None):
        self.capacity = capacity or DEFAULT_CAPACITY
        self.cache = {}


    def set(self, key, value):

        if len(self.cache) > self.capacity