# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            # If the current node is None, append "N" to the result list
            if not node:
                res.append("N")
                return
            # Append the value of the current node to the result list
            res.append(str(node.val))
            # Recursively serialize the left and right subtrees
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        # We use a class variable `index` to keep track 
        # of the current position in the list of values
        self.index = 0
        
        def dfs():
            if vals[self.index] == "N":
                self.index += 1
                return None
            
            # Create a new TreeNode with the current value
            node = TreeNode(int(vals[self.index]))
            # Move to the next value in the list
            self.index += 1
            # Recursively build the left and right subtrees
            node.left = dfs() # type: ignore
            node.right = dfs() # type: ignore
            # Return the constructed node/tree
            return node
        
        return dfs()