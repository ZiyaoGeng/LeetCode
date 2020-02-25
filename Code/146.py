import collections

class LRUCache:

    def __init__(self, capacity: int):
    	self.capacity = capacity
    	self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
    	if self.cache.get(key) == None:
    		return -1
    	else:
    		self.cache.move_to_end(key)
    		return self.cache[key]

    def put(self, key: int, value: int) -> None:
    	if key in self.cache:
    		self.cache.move_to_end(key)
    	self.cache[key] = value
    	if len(self.cache) > self.capacity:
    		self.cache.popitem(last=False)