class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Program:
    def makeATree(self, nums):
        root = TreeNode(nums[0])
        for i in range(1, len(nums)):
            self.insertValue(root, nums[i])
        return root
    
    def insertValue(self, root, val):
        if not root:
            root = TreeNode(val)
            return
        if root.val < val:
            if root.right:
                self.insertValue(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left:
                self.insertValue(root.left, val)
            else:
                root.left = TreeNode(val)
    
    def InOrderTraversal(self, root):
        res = []
        self._InOrderTraversal(root, res)
        print(res)
        return
    
    def _InOrderTraversal(self, root, res):
        if not root:
            return
        self._InOrderTraversal(root.left, res)
        res.append(root.val)
        self._InOrderTraversal(root.right, res)
    
    def cloneTree(self, root):
        if not root:
            return None
        
        from collections import deque
        ori_q = deque()
        new_q = deque()
        
        ori_q.append(root)
        new_tree = TreeNode(root.val)
        new_q.append(new_tree)
        
        while ori_q:
            ori_node = ori_q.popleft()
            new_node = new_q.popleft()
            if ori_node.left:
                ori_q.append(ori_node.left)
                new_node.left = TreeNode(ori_node.left.val)
                new_q.append(new_node.left)
            if ori_node.right:
                ori_q.append(ori_node.right)
                new_node.right = TreeNode(ori_node.right.val)
                new_q.append(new_node.right)
        return new_tree

# Test
p = Program()
root = p.makeATree([5,3,1,2,4,6,7,9])
p.InOrderTraversal(root)
# [1, 2, 3, 4, 5, 6, 7, 9]

root2 = p.cloneTree(root)
p.InOrderTraversal(root2)