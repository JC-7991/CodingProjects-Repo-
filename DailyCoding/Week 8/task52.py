# Implement an LRU (Least Recently Used) cache. It 
# should be able to be initialized with a cache size n, 
# and contain the following methods:
# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.

from LinkedList import *

class LRUCache:

  def __init__(self, capacity):

    self.capacity = capacity
    self.cache = set()
    self.cache_vals = LinkedList()

  def set(self, value):

    node = self.get(value)
    if node == None:

      if(self.cache_vals.size >= self.capacity):

        self.cache_vals.insert_at_tail(value)
        self.cache.add(value)
        self.cache.remove(self.cache_vals.get_head().data)
        self.cache_vals.remove_head()

      else:
        self.cache_vals.insert_at_tail(value)
        self.cache.add(value)
    
    else:
        self.cache_vals.remove(value)
        self.cache_vals.insert_at_tail(value)
  
  def get(self, value):

    if value not in self.cache:
        return None

    else:

        i = self.cache_vals.get_head()

        while i is not None:
            
            if i.data == value:
                return i
            i = i.next

  def printcache(self):

    node = self.cache_vals.get_head()

    while node != None :
        print(str(node.data) + ", ")
        node = node.next

if __name__ == "__main__":

    cache1 = LRUCache(4)
    cache1.set(10)
    cache1.printcache()

    cache1.set(15)
    cache1.printcache()

    cache1.set(20)
    cache1.printcache()