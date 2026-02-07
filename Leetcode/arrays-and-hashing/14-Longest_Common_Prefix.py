from typing import List

class Solution:
    # Time complexity: O(S) where S is the sum of all characters in all strings
    # Space complexity: O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Create empty string to store prefixes
        res = ""

        # For every character in the first string of the list "strs"
        for i in range(len(strs[0])):

            # For every item in the list strs
            for s in strs:
                # if i is greater than or equal to the item s at index i
                # or if the string s at index i DOES NOT equal the first string at index i
                if i >= len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
    # Time complexity: O(S) where S is the sum of all characters in all strings
    # Space complexity: O(1)
    def alternativeLongestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]: # Skip index 0 and start with 1 and go up to the end. Start with the second string
            while not s.startswith(prefix): # While the string s does not start with the prefix
                prefix = prefix[:-1] # Remove the last character from the prefix
                if not prefix: # If the prefix becomes empty
                    return ""
        return prefix