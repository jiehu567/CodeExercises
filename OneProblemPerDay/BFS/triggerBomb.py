class Solution:
    def triggerBomb(self, nums, i, j):
        if not nums or not nums[0] or \
                i<0 or i>=len(nums) or \
                j<0 or j>=len(nums[0]):
            return 0
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        from collections import deque
        q = deque()
        q.appendleft((i,j))
        
        while q:
            x, y = q.pop()
            nums[x][y] = 0
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if self.check(nums, nx, ny):
                    q.appendleft((nx, ny))

        return sum([sum(elem) for elem in nums])
    
    def check(self, nums, i, j):
        return 0<=i<len(nums) and 0<=j<len(nums[0]) and nums[i][j] == 1
                

# Test

nums = [
    [0,0,1,1,0,0],
    [0,0,1,1,0,1],
    [0,0,1,1,0,1],
    [0,0,1,1,0,1],
    [1,1,1,1,1,1],
    [0,0,1,1,0,0],
]

s = Solution()
s.triggerBomb(nums, 0, 0)
# 19

s.triggerBomb(nums, 0, 2)
# 0