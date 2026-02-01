from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Using Recursive Depth First Search (DFS)
        if not p and not q: # Both are null
            return True
        if not p or not q: # One is null (other isn't since the above would've passed)
            return False
        if p.val != q.val: # If p does not equal q
            return False

        # Rerun again, twice, this time p and q are the children
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
