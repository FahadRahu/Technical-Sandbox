class Solution:
    # Brute force approach
    def mySqrt(self, x: int) -> int:
        res = 0

        if x == 0 or x == 1:
            return x

        for i in range(x):
            temp = i*i
            if temp <= x:
                res = i
            if temp > x:
                break
        return res # type: ignore
    
    # Binary search approach
    def mySqrt2(self, x: int) -> int:
        res = 0

        if x == 0 or x == 1:
            return x
        
        l, r = 0, x
        
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                l = mid + 1 # Left pointer moves, right stays the same
            else: # mid * mid > x --> mid needs to be smaller
                r = mid - 1
        # We want to return the last mid that was <= x, which is r, because l will have moved one step past it
        return r
"""
Thoughts:
1. x is positive
2. Get sqrt
3. Round down to nearest integer
4. No built in functions

1. Take x
2. How to get square root?
    a. Sqrt is inherently x ^ 0.5

"""