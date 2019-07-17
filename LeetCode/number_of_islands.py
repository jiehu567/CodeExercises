class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        
        return count
    
    def check(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1'
    
    # def bfs(self, grid, i, j):
    #     dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    #     from collections import deque
    #     q = deque([[i, j]])
    #     grid[i][j] = '0'
    #     while q:
    #         x, y = q.popleft()
    #         for dx, dy in dirs:
    #             nx, ny = x+dx, y+dy
    #             if not self.check(grid, nx, ny):
    #                 continue
    #             q.append([nx, ny])
    #             grid[nx][ny] = '0'
    def dfs(self, grid, i, j):
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        stk = [[i, j]]
        grid[i][j] = '0'

        while stk:
            x, y = stk.pop()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if not self.check(grid, nx, ny):
                    continue
                stk.append([nx, ny])
                grid[nx][ny] = '0'