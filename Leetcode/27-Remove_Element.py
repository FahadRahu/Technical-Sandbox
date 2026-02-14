from typing import List

class Solution:
    # Time complexity: O(n) | Space complexity: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
        
        # Example (nums=[3,2,2,3], val=3):
            # i=0 skip -> k=0, nums=[3,2,2,3]
            # i=1 keep -> nums[0]=2, k=1, nums=[2,2,2,3]
            # i=2 keep -> nums[1]=2, k=2, nums=[2,2,2,3]
            # i=3 skip -> k=2, nums=[2,2,2,3]    