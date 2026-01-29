from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case - if the node is None, return None, everything below is already inverted
        if not root:
            return None
        
        # Swap the left and right children of the current node - this inverts the current node
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Recursively invert the left and right subtrees - this inverts the rest of the tree below the current node
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root