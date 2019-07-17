# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0
        
        max_avg, node_sum, node_num = self.helper(root)
        return max_avg
    
    def helper(self, root):
        if not root:
            return 0, 0, 0
        
        max_avg_l, node_sum_l, node_num_l = self.helper(root.left)
        max_avg_r, node_sum_r, node_num_r = self.helper(root.right)
        cur_sum = node_sum_l + node_sum_r + root.val
        cur_node_num = node_num_l + node_num_r + 1
        cur_avg = cur_sum / cur_node_num
        if max_avg_l == max(max_avg_l, cur_avg, max_avg_r):
            return max_avg_l, cur_sum, cur_node_num
        if max_avg_r == max(max_avg_l, cur_avg, max_avg_r):
            return max_avg_r, cur_sum, cur_node_num
        return cur_avg, cur_sum, cur_node_num