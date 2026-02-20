from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf") )
    
    """
        Validates a Binary Search Tree using range checking at each node.
        
        Algorithm:
        - Each node must have a value within a valid range (left, right)
        - All left descendants must be less than the node's value
        - All right descendants must be greater than the node's value
        
        How the bounds work:
        - valid(node.left, left, node.val): Left subtree keeps the lower bound,
          but the upper bound becomes node.val to ensure ALL left descendants < node
        - valid(node.right, node.val, right): Right subtree keeps the upper bound,
          but the lower bound becomes node.val to ensure ALL right descendants > node
        
        Example trace (Root → Left → Right → Right):
        
                20
               /  \
              10   30
             / \
            5   15
               /  \
              12   18
                    \
                     19
        
        Tracing node 19:
        1. valid(20, -inf, inf)   → Bounds: (-inf, inf)
        2. valid(10, -inf, 20)    → Go LEFT: bounds become (-inf, 20)
        3. valid(15, 10, 20)      → Go RIGHT: bounds become (10, 20)
        4. valid(18, 15, 20)      → Go RIGHT: bounds become (15, 20)
        5. valid(19, 18, 20)      → Go RIGHT: bounds become (18, 20)
        
        The bounds (18, 20) automatically enforce that 19 must be:
        - Greater than 18, 15, 10 (all ancestors on the path)
        - Less than 20 (the root we descended left from)
        
        All ancestor constraints encoded in just two numbers!
        """
    