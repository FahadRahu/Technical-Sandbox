from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time Complexity: O(m * n) in the worst case, where m and n are the number of nodes in root and subRoot respectively.
    # Space Complexity: O(h) where h is the height of the tree due to recursion stack.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        
        return False

    # Helper function to check if two trees are identical
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return(self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False