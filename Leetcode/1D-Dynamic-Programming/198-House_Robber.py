from typing import List

class Solution:
    # Time: O(n)
    # Space: O(1)

    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    """Explanation: We can use two variables to keep track of the maximum amount of money 
    that can be robbed up to the current house. The variable `rob1` will store the maximum 
    amount of money that can be robbed from two houses down, while `rob2` will store 
    the maximum amount of money that can be robbed from the previous house. For each house, 
    we calculate the maximum amount of money that can be robbed by either robbing the current 
    house and adding it to `rob1`, or by not robbing the current house and keeping `rob2`. 
    We then update `rob1` and `rob2` accordingly. Finally, we return `rob2`, which will 
    contain the maximum amount of money that can be robbed from all the houses."""