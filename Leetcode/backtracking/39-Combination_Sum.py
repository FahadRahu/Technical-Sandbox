from typing import List

"""
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers 
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two 
combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that 
sum up to target is less than 150 combinations for the given input.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # Final list of valid combinations

        def dfs(i, cur, total):
            # Base case 1: we hit the target exactly, so save this combination
            if total == target: 
                res.append(cur.copy())
                return
            # Base case 2: out of bounds or too large, so stop exploring
            if i >= len(candidates) or total > target:
                return
            
            # Choice 1: include the current candidate again (can reuse it)
            cur.append(candidates[i]) # Add the current candidate to the combination
            dfs(i, cur, total + candidates[i]) # Recurse with the same index to allow reuse
            cur.pop()  # Backtrack to try the other choice

            # Choice 2: skip the current candidate and move to the next one
            dfs(i + 1, cur, total) # Recurse with the next index to skip the current candidate

        # Start exploring from index 0 with an empty combination and total 0
        dfs(0, [], 0)
        return res

"""
Start
Candidates = [2,3], target = 7


dfs(0, [], 0)
├─ Include 2 → dfs(0, [2], 2)
│  ├─ Include 2 → dfs(0, [2,2], 4)
│  │  ├─ Include 2 → dfs(0, [2,2,2], 6)
│  │  │  ├─ Include 2 → dfs(0, [2,2,2,2], 8)  (too big, stop)
│  │  │  └─ Skip 2 → dfs(1, [2,2,2], 6)
│  │  │     ├─ Include 3 → dfs(1, [2,2,2,3], 9)  (too big, stop)
│  │  │     └─ Skip 3 → dfs(2, [2,2,2], 6)     (out of bounds, stop)
│  │  └─ Skip 2 → dfs(1, [2,2], 4)
│  │     ├─ Include 3 → dfs(1, [2,2,3], 7)  ✅ hit target, save [2,2,3]
│  │     └─ Skip 3 → dfs(2, [2,2], 4)       (out of bounds, stop)
│  └─ Skip 2 → dfs(1, [2], 2)
│     ├─ Include 3 → dfs(1, [2,3], 5)
│     │  ├─ Include 3 → dfs(1, [2,3,3], 8)  (too big, stop)
│     │  └─ Skip 3 → dfs(2, [2,3], 5)       (out of bounds, stop)
│     └─ Skip 3 → dfs(2, [2], 2)            (out of bounds, stop)
└─ Skip 2 → dfs(1, [], 0)
   ├─ Include 3 → dfs(1, [3], 3)
   │  ├─ Include 3 → dfs(1, [3,3], 6)
   │  │  ├─ Include 3 → dfs(1, [3,3,3], 9)  (too big, stop)
   │  │  └─ Skip 3 → dfs(2, [3,3], 6)       (out of bounds, stop)
   │  └─ Skip 3 → dfs(2, [3], 3)            (out of bounds, stop)
   └─ Skip 3 → dfs(2, [], 0)                (out of bounds, stop)
"""