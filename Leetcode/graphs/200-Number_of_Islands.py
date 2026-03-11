from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        # The point of this function is to perform a BFS starting from a given cell (r, c) and mark all connected land cells as visited
        def bfs(r, c):
            # Initialize the BFS queue with the starting cell and add it to the visited set
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            
            # Continue the BFS until all connected land cells are visited
            while queue:
                # Dequeue the next cell to process (first in, first out)
                row, col = queue.popleft()
                # Explore all 4 possible directions (up, down, left, right)
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                # Check each neighboring cell
                for dr, dc in directions:
                    # Make it easier to reference the neighboring cell by calculating its row and column indices
                    nr, nc = row + dr, col + dc

                    # If the neighboring cell is within bounds, is land, and has not been visited, add it to the queue
                    # Could have used nr in range(rows) and nc in range(cols)
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visit:
                        # Add the neighboring cell to the queue to be processed and mark it as visited
                        queue.append((nr, nc))
                        visit.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Start a BFS from the current cell to mark all connected land cells
                    bfs(r, c)
                    islands += 1
        return islands