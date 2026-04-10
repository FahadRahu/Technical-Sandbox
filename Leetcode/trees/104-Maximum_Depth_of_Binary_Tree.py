from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Approach: Recursive Depth-First Search (DFS)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    
    # Approach: Iterative Depth-First Search (DFS) using Stack
    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree
        if not root:
            return 0
        
        # Stack will hold tuples of (node, depth)
        stack: list[tuple[Optional[TreeNode], int]] = [(root, 1)] 
        # Variable to keep track of the maximum depth encountered
        max_depth = 0
        
        while stack: # Loop until there are nodes to process in the stack
            node, depth = stack.pop() # Get the current node and its depth from the stack
            if node:
                max_depth = max(max_depth, depth) # Update max_depth if current depth is greater
                stack.append((node.left, depth + 1)) # Add left child to stack with incremented depth
                stack.append((node.right, depth + 1)) # Add right child to stack with incremented depth
        
        return max_depth
    
    # Approach: Iterative Breadth-First Search (BFS) using Queue
    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n) | Space Complexity: O(w) where w is the maximum width of the tree
        if not root:
            return 0
        
        from collections import deque
        queue: deque[tuple[Optional[TreeNode], int]] = deque([(root, 1)])
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            if node:
                max_depth = max(max_depth, depth) # Update max_depth if current depth is greater
                queue.append((node.left, depth + 1)) # Add left child to queue with incremented depth
                queue.append((node.right, depth + 1)) # Add right child to queue with incremented depth
        
        return max_depth

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case - empty root
        if not root:
            return 0
        
        # Using recursion
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))