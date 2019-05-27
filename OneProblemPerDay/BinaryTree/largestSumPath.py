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
    
    def reverseTree(self, root):
        if not root:
            return
        
        self.reverseTree(root.left)
        self.reverseTree(root.right)
        root.left, root.right = root.right, root.left
        
    def largestSumPathRecursive(self, root):
        return self._largestSumPathRecursive(root)
    
    def _largestSumPathRecursive(self, root):
        if not root:
            return 0
        
        l = self._largestSumPathRecursive(root.left)
        r = self._largestSumPathRecursive(root.right)
        return max(l, r) + root.val
        
    def largestSumPathIter(self, root):
        if not root:
            return 0
        s = [root]
        res = 0
        cur = 0
        while s:
            tmp = s.pop()
            cur += tmp.val
            if not tmp.left and not tmp.right:
                res = max(res, cur)
                cur -= tmp.val
            if tmp.left:
                s.append(tmp.left)
            if tmp.right:
                s.append(tmp.right)
        return res

# Test
p = Program()
root = p.makeATree([5,3,1,2,4,6,7,9])
p.InOrderTraversal(root)
# p.reverseTree(root)
# p.InOrderTraversal(root)
p.largestSumPathRecursive(root)
# 27
p.largestSumPathIter(root)
# 27
