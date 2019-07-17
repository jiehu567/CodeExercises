# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # count = 1
        # count_left = self.countNodes(root.left) if root.left else 0
        # count_right = self.countNodes(root.right) if root.right else 0
        # count += (count_left + count_right)
        # return count
        count = 0
        from collections import deque
        q = deque([root])
        while q:
            tmp = q.popleft()
            count+=1
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        return count