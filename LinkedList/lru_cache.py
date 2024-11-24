# LRU Cache

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.

# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. 
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.map = {}
        self.start = ListNode(-1, -1)
        self.end = ListNode(-1, -1)
        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.map:
            old_node = self.map[key]
            self.remove(old_node)
        
        node = ListNode(key, value)
        self.map[key] = node
        self.add(node)

        if len(self.map) > self.cap:
            remove_node = self.start.next
            self.remove(remove_node)
            del self.map[remove_node.key]

    def add(self, node):
        prev_end = self.end.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.end
        self.end.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

if __name__ == "__main__":
    LRUCache = LRUCache()
    LRUCache.put(1, 1)  # cache is {1=1}
    LRUCache.put(2, 2); # cache is {1=1, 2=2}
    LRUCache.get(1);    # return 1
    LRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    LRUCache.get(2);    # returns -1 (not found)
    LRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    LRUCache.get(1);    # return -1 (not found)
    LRUCache.get(3);    # return 3
    LRUCache.get(4);    # return 4

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)