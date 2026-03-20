class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        # We COULD have just used an array to store each number of valid steps from n to 0 (bottom up)
        # BUT that would take up O(n) space complexity. Using just what you need with "one" and "two" makes 
        # the space complexity O(1). Time complexity is still O(n) because we have to loop through n-1 times to get the answer.
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one
    
    """
                Return the number of distinct ways to climb to step `n`
                when you can move either 1 or 2 steps at a time.

                Idea (bottom-up dynamic programming, O(1) space):
                - Let ways(k) be the number of ways to reach step k.
                - To get to step k, your last move must come from:
                    1) step k-1 (taking 1 step), or
                    2) step k-2 (taking 2 steps)
                - So: ways(k) = ways(k-1) + ways(k-2)
                    (this is the Fibonacci pattern).

                Instead of storing all previous values, we only keep the latest two:
                - `one` = current ways(k-1)
                - `two` = current ways(k-2)
                Each loop shifts the window forward by one step.

                Visual trace for n = 5:
                Start: one=1, two=1   (base: ways(1)=1, ways(0)=1)
                i=0 -> one=2, two=1   (ways(2)=2)
                i=1 -> one=3, two=2   (ways(3)=3)
                i=2 -> one=5, two=3   (ways(4)=5)
                i=3 -> one=8, two=5   (ways(5)=8)
                Return one = 8

                Complexity:
                - Time: O(n)
                - Space: O(1)
                """