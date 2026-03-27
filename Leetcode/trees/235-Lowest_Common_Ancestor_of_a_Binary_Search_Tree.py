# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
        
        # This line should never be reached since p and q are guaranteed to be in the tree
        return root
    
class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode: # type: ignore
        """Thoughts:
        - How far down cann we go while having a common ancestor?
        - Keep going down binary tree until curr (node we're looking at) is between p and q and return
        - Edge cases:
            1. What if there is no root? Return none
            2. What if curr == q or p? Return that node, going further won't make them common since we'd have passed q or p anyways. 
        """

        curr = root
        
        if not root:
            return None
        # If we DO have a root, check if less than p/q, greater than p/q, equal, or in between
        
        while curr:
            if curr.val > p.val and curr.val > q.val: # and root? we checked above tho
                # Curr is HIGH, let's go left to find a lower value
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                # Curr is LOW, let's go right and find a BIGGER value
                curr = curr.right
            
            # The above considers if p/q is BOTH above, or both below
            # What if one above and one below? OR if curr == p and/or q?

            else: # Considers in between and matches
                return curr