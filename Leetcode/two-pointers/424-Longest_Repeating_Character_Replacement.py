class Solution:
    # Time Complexity: O(n) | Space Complexity: O(1) since we are only storing 26 characters in the hash map
    def characterReplacement(self, s: str, k: int) -> int:
        # Magic formula is --> substring_len - max_freq <= k
        # We are looking for the longest substring_len while the above is true
        
        # Create empty hash map
        count = {}
        
        res = 0
        l = 0
        maxf = 0

        # Iterate through the string s with our right pointer
        for r in range(len(s)):
            # Add 1 to current right pointer to hash map, if it's empty, default as 0 then add 1
            count[s[r]] = 1 + count.get(s[r], 0)
            # Update maxf to whatever is higher, this is way faster than checking entire HM each iteration
            maxf = max(maxf, count[s[r]])

            # If the magic formula ends up False (greater than k)
            while (r - l + 1) - maxf > k:
                # Edit our hashmap to decrease what the left pointer is at since it's being pushed right 1
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res