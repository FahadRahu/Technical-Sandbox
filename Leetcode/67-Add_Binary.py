class Solution:
# Re-Solved 4/27/2026
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1] # Start(Inc.) | Stop(Exc.) | Skip(-1 = Start at End)

        for i in range(max(len(a), len(b))): # We'll iterate thru whichever larger string
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0 #ord gives you the ASCII value of whatever's inputted
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0 # if cur iteration < len of our string

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        
        if carry:
            res = '1' + res
        return res