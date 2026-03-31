import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        
        # Letter: Amount of times it shows up
        chars = {}
        # Fill hashmap with chars:freq
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        
        # We need a heap to keep track of the MOST frequent element
        # Python doesn't have max heaps, so we'll use a min heap with freq as neg numbers
        maxHeap = [] # Creates an empty list
        for char, freq in chars.items(): # For each pair in chars
            maxHeap.append([-freq, char]) # Append that pair (-freq, char) to the list maxHeap
        
        # Now we need to make a heap out of maxHeap
        heapq.heapify(maxHeap) # This makes a heap out of the list maxHeap - runs in ~O(n) time

        prev = None # We need to remember not to place to same chars next to each other
        res = "" # Result string we're building

        while maxHeap or prev: # If we haven't burned thru maxHeap yet, OR if we're still at freq > 0
            if not maxHeap and prev: # No more left in the bank WITHOUT repeating strings
                return ""

            freq, char = heapq.heappop(maxHeap) # Removes from heap, we access the item pair
            res += char # Add character to our res string we are building
            freq += 1

            if prev: # If prev is not None/Null
                heapq.heappush(maxHeap, prev) # We can push the OLD prev from the previous iteration back to heap
                prev = None
            if freq != 0: # This only matters if there's still some of that character left in the bank after the +1
                prev = [freq, char]
        
        return res
"""
Thoughts:
1. We're going to iterate thru our string, and add each character to our hashmap as a key
    a. Key = character in s
    b. Value = # Times it shows up
    c. Notes: Probably going to have to use the .get() func to make default when retrieving key!
    d. How are we going to get an order of most frequent?
"""