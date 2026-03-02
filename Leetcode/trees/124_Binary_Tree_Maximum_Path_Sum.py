from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        res = [root.val] # type: ignore

        # Return maximum path sum starting from this node
        def dfs(root):
            if not root:
                return 0
            
            # Compute the maximum path sum starting from the left and right child
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            # Ignore negative paths, as they would decrease the overall path sum
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update the global maximum path sum if the path through this node is larger
            # Compute the maximum path sum with split
            res[0] = max(res[0], leftMax + rightMax + root.val)
           
            # Return the maximum path sum starting from this node
            return max(leftMax, rightMax) + root.val

        dfs(root)
        return res[0]
    
"""
        Find the maximum path sum in a binary tree where a path can start and end at any nodes.
        
        KEY INSIGHT:
        - At each node, we track TWO different things:
          1. What we RETURN: max path sum going DOWN from this node (to pass up to parent)
          2. What we UPDATE in res: max path sum THROUGH this node (left + node + right)
        
        ALGORITHM:
        1. Use DFS to visit each node
        2. At each node, calculate the maximum path sum going down left and right subtrees
        3. Ignore negative paths (they decrease the sum)
        4. Update global max with the path THROUGH current node: leftMax + rightMax + node.val
        5. Return to parent the best path DOWN from current node: max(leftMax, rightMax) + node.val
        
        EXAMPLE WALKTHROUGH: root = [-10,9,20,null,null,15,7]
        
        Tree structure:
                -10
               /   \
              9     20
                   /  \
                  15   7
        
        DFS execution (post-order traversal):
        
        Step 1: DFS(15) - leaf node
            - No children, return 0 for both left and right
            - leftMax = max(0, 0) = 0
            - rightMax = max(0, 0) = 0
            - Update res[0] = max(-10, 0 + 0 + 15) = 15
            - Return: max(0, 0) + 15 = 15
            - res = [15]
        
        Step 2: DFS(7) - leaf node
            - No children, return 0 for both
            - leftMax = 0, rightMax = 0
            - Update res[0] = max(15, 0 + 0 + 7) = 15
            - Return: max(0, 0) + 7 = 7
            - res = [15]
        
        Step 3: DFS(20) - has two children
            - leftMax = DFS(15) = 15
            - rightMax = DFS(7) = 7
            - leftMax = max(15, 0) = 15
            - rightMax = max(7, 0) = 7
            - Update res[0] = max(15, 15 + 7 + 20) = max(15, 42) = 42  ← This is the path 15→20→7
            - Return: max(15, 7) + 20 = 35 (best path going DOWN from node 20)
            - res = [42]
        
        Step 4: DFS(9) - leaf node
            - No children
            - leftMax = 0, rightMax = 0
            - Update res[0] = max(42, 0 + 0 + 9) = 42
            - Return: max(0, 0) + 9 = 9
            - res = [42]
        
        Step 5: DFS(-10) - root node
            - leftMax = DFS(9) = 9
            - rightMax = DFS(20) = 35
            - leftMax = max(9, 0) = 9
            - rightMax = max(35, 0) = 35
            - Update res[0] = max(42, 9 + 35 + (-10)) = max(42, 34) = 42
            - Return: max(9, 35) + (-10) = 25 (not used since this is root)
            - res = [42]
        
        Final answer: 42 (the path 15 → 20 → 7)
        
        WHY THIS WORKS:
        - We consider every possible path by checking what happens if each node is the "peak" of the path
        - By returning max(leftMax, rightMax) + node.val, we ensure parent nodes can extend paths
        - By updating res with leftMax + rightMax + node.val, we capture paths that "turn" at this node
        """