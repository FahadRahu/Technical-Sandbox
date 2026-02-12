from typing import List

class Solution:
    # Time complexity: O(log n) | Space complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        # Initialize our pointers
        l, r = 0, len(nums) - 1
        
        # We will loop until our pointers are the same or they cross each other
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # m is left bound, shift is to the right
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            else: # nums[m] < nums[l] --> m is right bound, shift is to the left
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1