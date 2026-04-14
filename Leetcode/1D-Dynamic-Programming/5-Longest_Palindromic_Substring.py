class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Best palindrome substring found so far and its length.
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # Odd-length palindrome: center is exactly at i.
            l, r = i, i
            # Expand while both pointers are in bounds and characters mirror each other.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Even-length palindrome: center is between i and i + 1.
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res