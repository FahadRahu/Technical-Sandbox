class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
    
    def alternativeLengthOfLastWord(self, s: str) -> int:
        # i is the last index of the string
        # length is the length of the last word, current set to zero
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length