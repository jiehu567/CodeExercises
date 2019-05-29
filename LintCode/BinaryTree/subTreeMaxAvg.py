# Subtree with Maximum Average

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    avg = 0
    node = None
    
    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.node
    
    def helper(self, root):
        if not root:
            return 0, 0  # sum, size
        
        l_sum, l_size = self.helper(root.left)
        r_sum, r_size = self.helper(root.right)
        
        s = l_sum + r_sum + root.val
        size = l_size + r_size + 1
        avg = s / size
        if self.node is None or avg > self.avg:
            self.avg = avg
            self.node = root
        return s, size
            
        