from typing import List
import heapq

class Solution:
    # Approach: Bucket Sort
    # Time Complexity: O(n) | Space Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq= [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res # We don't actually reach here given the problem constraints
    
    # Approach: Heap
    # Time Complexity: O(n log k) | Space Complexity: O(n)
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element - index is the element, value is the frequency
        count = {}

        # Build the frequency map
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Build a min-heap of size k - the heap will store tuples of (frequency, element)
        heap = []
        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the elements from the heap
        res = []

        # Since it's a min-heap, we pop the smallest frequency first
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res[::-1]  # Reverse to get the most frequent elements first