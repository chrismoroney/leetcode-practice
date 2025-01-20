# LRU Cache

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.

# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. 
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.

import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dictionary = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1

        self.dictionary.move_to_end(key)
        return self.dictionary[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary.move_to_end(key)

        self.dictionary[key] = value
        if len(self.dictionary) > self.cap:
            self.dictionary.popitem(last=False)

if __name__ == "__main__":
    LRUCache = LRUCache(2)
    LRUCache.put(1, 1)  # cache is {1=1}
    LRUCache.put(2, 2); # cache is {1=1, 2=2}
    LRUCache.get(1);    # return 1
    LRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    LRUCache.get(2);    # returns -1 (not found)
    LRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    LRUCache.get(1);    # return -1 (not found)
    LRUCache.get(3);    # return 3
    LRUCache.get(4);    # return 4
    print(LRUCache.dictionary)
    print(LRUCache.get(1))
    print(LRUCache.get(2))
    print(LRUCache.get(3))
    print(LRUCache.get(4))
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)