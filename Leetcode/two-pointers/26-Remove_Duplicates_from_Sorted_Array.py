from typing import List

class Solution:
    # Time Complexity: O(n) | Space Complexity: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        # Don't really need this, leetcode says the array is non-empty
        if not nums:
            return 0
        
        # l is the index of the last unique element in the array
        l = 1

        for r in range(1, len(nums)):
            # If the current element is different from the previous one, it's a unique element
            if nums[r] != nums[r - 1]: 
                nums[l] = nums[r]
                l += 1
        return l