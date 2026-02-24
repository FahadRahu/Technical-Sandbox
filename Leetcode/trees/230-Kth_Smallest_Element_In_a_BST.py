from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Time Complexity: O(H + k), where H is the height of the tree
    # In the worst case, H can be equal to N (when the tree is skewed), so the time complexity can be O(N + k).
    # Space Complexity: O(H), where H is the height of the tree
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0: # We don't need "and root" because the problem guarantees that k < total num nodes
                return root.val # type: ignore
            root = root.right # type: ignore
    # We don't need to check if stack is true because we will always have a node to process 
    # until we find the k-th smallest element since the problem guarantees that k is valid 
    # (1 ≤ k ≤ number of nodes in the tree). Otherwise, we would have to check if stack is 
    # empty before popping to avoid an error.
    

    # Neetcode Solution
    # Time Complexity: O(H + k), where H is the height of the tree
    # Space Complexity: O(H), where H is the height of the tree
    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int: # type: ignore
        n = 0 # Number of nodes visited
        stack = [] # Stack to hold nodes for in-order traversal
        cur = root # Current node being processed

        while cur and stack: # While there are nodes to process
            while cur: # Traverse left subtree
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop() # Get the next node in in-order sequence
            n += 1 # Increment count of nodes visited
            
            if n == k: # If we've reached the k-th smallest, return its value
                return cur.val
            
            cur = cur.right # Move to the right subtree for further processing
    

    # Time Complexity: O(H + k), where H is the height of the tree
    # Space Complexity: O(H), where H is the height of the tree
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return self.result # type: ignore
