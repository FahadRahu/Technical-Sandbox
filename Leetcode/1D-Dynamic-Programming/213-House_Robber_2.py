from typing import List

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def rob(self, nums: List[int]) -> int:
        # Edge case: If there is only one house, return the amount in that house
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    
    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

"""Explanation:
The problem is a variation of the classic "House Robber" problem, where the houses 
are arranged in a circle. This means that the first and last houses are adjacent, 
and you cannot rob both of them. To solve this problem, we can break it down into 
two separate cases:

1. Rob the first house and skip the last house: In this case, we can only consider the 
   houses from the second to the last house (nums[1:]).
2. Skip the first house and rob the last house: In this case, we can only consider the 
   houses from the first to the second-to-last house (nums[:-1]).

We can then use a helper function to calculate the maximum amount that can be robbed 
for each of these cases, and return the maximum of the two results. The helper function 
implements the standard "House Robber" dynamic programming approach, where we keep track 
of the maximum amount that can be robbed up to the current house without robbing adjacent 
houses. The time complexity of this solution is O(n) and the space complexity is O(1) 
since we are using only a constant amount of extra space for the variables.
"""

class HouseRobber1:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2