class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base case if either string is empty
        if t == "" or s == "":
            return ""

        # Count the frequency of each character in t
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Number of unique characters in t that need to be present in the window
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        # Expand the window with the right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # If the current character is part of t and its frequency in the window matches the required frequency in t
            if c in countT and window[c] == countT[c]:
                have += 1

            # Needs to be a loop because we want to shrink the window from the left as much as possible while still maintaining all required characters
            while have == need:
                # Update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # Pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""