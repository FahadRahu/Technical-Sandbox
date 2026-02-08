class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create an empty set for the substrings we add later
        charSet = set()
        # Establish left pointer and res variable
        l = 0
        res = 0

        # Iterate through right pointer starting from beginning
        for r in range(len(s)):
            # If our right pointer is in our set, we need to push left to get rid of it
            # We use while because we need to KEEP GOING until the repeat is gone
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet)) # Instead of charSet.size, could have done "r - l + 1"
        return res