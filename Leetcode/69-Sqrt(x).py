class Solution:
    def mySqrt(self, x: int) -> int:
        res = None

        for i in range(x):
            temp = i*i
            if temp <= x:
                res = i
            if temp > x:
                break
        return res # type: ignore

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