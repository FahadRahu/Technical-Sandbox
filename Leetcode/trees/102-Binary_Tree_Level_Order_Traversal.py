from typing import List, Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        # Breath first search (BFS)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft() # pops the leftmost element in the queue (whatever was added first - lowest index)
                if node: # if node is not None, "None" gets added to the queue even when the current node is at its end
                    level.append(node.val) # Add the value of the current node to the level list
                    q.append(node.left) # Add the left child of the current node to the queue
                    q.append(node.right) # Add the right child of the current node to the queue
            if level:
                res.append(level)
        return res
    
    """ 
        BFS Level-Order Traversal: Returns tree nodes grouped by level.
        
        Visual Example:
                3
               / \
              9   20
                 /  \
                15   7
        
        Step-by-step execution:
        
        Iteration 1 (Level 0):
            Queue: [3]
            qLen = 1 (freeze current level size)
            Process: Pop 3, add to level, append children (9, 20)
            Result: res = [[3]], Queue = [9, 20]
        
        Iteration 2 (Level 1):
            Queue: [9, 20]
            qLen = 2 (freeze current level size)
            Process: Pop 9 (children: None, None), Pop 20 (children: 15, 7)
            Result: res = [[3], [9, 20]], Queue = [None, None, 15, 7]
        
        Iteration 3 (Level 2):
            Queue: [None, None, 15, 7]
            qLen = 4
            Process: Skip two Nones, Pop 15, Pop 7
            Result: res = [[3], [9, 20], [15, 7]]
        
        Key Insight:
        - qLen = len(q) "freezes" the current level's size
        - The for loop processes exactly qLen nodes (current level)
        - While processing, children are added for the NEXT level
        - None values are literally added to queue when nodes have no children
        - "if node:" check prevents errors when popping None values
        
        This naturally separates the tree into levels!
    """