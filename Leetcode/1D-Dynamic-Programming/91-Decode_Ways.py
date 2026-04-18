class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] stores the number of ways to decode the substring s[i:]
        # If we reach the end of the string, that counts as 1 valid decoding.
        dp = {len(s): 1}

        def dfs(i):
            # If this index was already solved before, reuse the answer.
            if i in dp:
                return dp[i]

            # A substring starting with "0" cannot be decoded.
            if s[i] == "0":
                return 0

            # Try taking one digit first.
            res = dfs(i + 1)

            # If the next two digits form a valid number from 10 to 26,
            # then we can also decode them together as one letter.
            if (
                i + 1 < len(s)
                and (
                    s[i] == "1"
                    or (s[i] == "2" and s[i + 1] in "0123456")
                )
            ):
                res += dfs(i + 2)

            # Save the answer for this index so we do not recompute it.
            dp[i] = res
            return res

        # Start decoding from the first character.
        return dfs(0)


# Annotation:
# This solution uses DFS + memoization (top-down dynamic programming).
# At each index, it explores:
# 1. Taking one digit as a letter
# 2. Taking two digits as a letter, if the number is between 10 and 26
#
# It adds the number of valid ways from both choices and stores the result
# in dp. Because each index is solved only once, the algorithm is efficient:
# Time Complexity: O(n)
# Space Complexity: O(n)