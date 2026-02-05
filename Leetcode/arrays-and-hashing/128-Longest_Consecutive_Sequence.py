from typing import List

class Solution:
    # Time complexity: O(n), Space complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) lookups
        numSet = set(nums)
        # Initialize the longest consecutive sequence length, starting from 0
        longest = 0

        for n in numSet:
            # Check if it's the start of a sequence (i.e., the previous number is not in the set)
            if (n - 1) not in numSet:
                length = 0
                # Count the length of the consecutive sequence starting from n
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
    # Time complexity: O(n log n), Space complexity: O(1)
    # This approach isn't acceptable since the question asks for O(n) time complexity
    def alternativeApproach(self, nums: List[int]) -> int:
        # Check if the list is empty
        if not nums:
            return 0
        
        # Sort the list to remove duplicates and find consecutive sequences
        nums.sort()
        longest = 1
        current = 1

        # Iterate through the sorted list, inclusive of 1, exclusive of len(nums)
        # So it goes up to len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Skip duplicates
                if nums[i] == nums[i - 1] + 1: # Check if the current number is consecutive
                    current += 1
                else:
                    longest = max(longest, current)  # Update the longest sequence length
                    current = 1  # Reset the current sequence length
        return max(longest, current)  # Return the maximum of the longest and current sequence lengths