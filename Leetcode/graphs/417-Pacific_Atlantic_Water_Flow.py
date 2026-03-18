from typing import List

class Solution:
    # Time Complexity: O(M*N) - M = number of rows and N = number of columns in the heights matrix. 
    #       We perform a DFS for each cell on the borders, which takes O(M*N) time in total.
    # Space Complexity: O(M*N) in the worst case, if all cells are visited during the DFS. 
    #       The space is used for the visited sets and the recursion stack.
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for c in range(COLS):
            # First Row, from left to right, does it reach the pacific?
            dfs(0, c, pac, heights[0][c])
            # Last Row, from left to right, does it reach the atlantic?
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            # First column, starting from the top going down, does it reach pacific?
            dfs(r, 0, pac, heights[r][0])
            # Last column, starting from the top going down, does it reach atlantic?
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res