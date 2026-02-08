from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
    
    # Brute force approach
    # Time complexity: O(n^2), Space complexity: O(1)
    def bruteForce(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area