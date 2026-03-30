class Node:
    def __init__(self, key, value):
        # Data
        self.key, self.value = key, value
        # Pointers
        self.left, self.right = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize our cache which is our hash map. Our cache size CANNOT be greater than size capacity
        self.capacity = capacity
        # Key is just key, value is a Node object 
        self.cache = {}
    
    # Remove the node from the DLL
    def remove(self, Node):
        pass
    
    # Insert a given node at the end of a DLL
    def insert(self, Node):
        pass

    def get(self, key: int) -> int:
        # Get the value of the key if it exists, else return -1
        if key in self.cache:
            # We need to return the value, AND push it to the right of the DLL
            # Step 1 - Moving to the right of DLL
            self.remove(self.cache[key]) # The node is value in cache
            self.insert(self.cache[key])
            # Step 2 is returning the value
            return self.cache[key].value

        return -1
        
    def put(self, key: int, value: int) -> None:
        # If that key we are trying to put is already in cache, it needs to be removed first
        if key in self.cache:
            self.remove[self.cache[key]]
        self.cache[key] = Node(key, value) # Add the key:value(Node) to cache
        self.insert(self.cache[key]) # Change the DLL such that this new key is right-oriented

        # Now we have to deal with the case where cache len == capacity (too big! get rid of LRU)
        if len(self.cache) > self.capacity:
            lru = self.left.next # Remember left is default val, the .next is the LRU
            self.remove(lru)
            del self.cache[lru.key]

"""
Thoughts:

Constraints:
1. LRU Cache (the hash map) size cannot be greater than capacity!
2. We need a way to find the OLDEST accessed item in the cache!
    1. Looking at it (get func) OR adding item (put func) both consider item accessed (newer).
    2. Use a doubly linked list!

Oldest | [1, 1] [2, 2] | Newest
Lets say you "get" [1, 1]. 

- We need a double linked list (we need to know the next connection AND previous connectionz)
- Need to create a node class that makes a node with a prev and next connection
- Main cache is a hash map. So we can have a key:value where value is a node? Maybe?
- Need a way to remove from linked list, and a way to insert to the right at the linked list


"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
The Graveyard of Failed Attempts:

3/29/2026
The Following is my first attempt at solving the problem.

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize positive size capacity
        # Need a hashmap of size capacity
        self.capacity = capacity
        self.cache = {} # items can't exceed capacity
        self.arr = []

    def get(self, key: int) -> int:
        temp = self.cache.get(key, -1) # temp = -1 or an existing key in cache
        if temp != -1: # If temp indeed in cache, we have to update that the key was accessed
            # We have to push to the front of array! That means key exists in cache
            if temp in self.arr:
                self.arr.remove(temp)
            self.arr.append(temp)

        # Return the value of key if true, else -1
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        # Hash map, update key otherwise add the new key
        if len(self.cache) >= self.capacity:
            # Get rid of the last accessed key
            remove = self.arr[0]
            self.cache.pop(remove)

        # Append key:value to cache!
        return self.cache[key] = value
   
        Two conditions:
        1. First we have to check if cache is full, if so, we have to remove oldest item
        2. Append the new key/value into the cache!
        3. How to make put func operate:
            1. Check if cache == capacity. If it does we have to make space for cache by removing oldest itemm
        



Thoughts:
1. Hash map definitely being used.
    a. The get function gives value of key
2. A few things to handle:
    1. The size of our hash map cannot exceed capacity (our input in init)
    2. What was the last accessed item in our hashmap? That is the item
        that is getting replaced if there is a new put!
3. How are we checking what the oldest accessed item is?
    a. What if we used a list! Maybe a stack? It's LIFO.
        1. every time we access a item, it gets pushed to the right of an array
            we can just access arr[0] for the item thats first
            every time an item is added or looked at, that key pushed to the far right of arr!

IDK how to solve this :(

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
