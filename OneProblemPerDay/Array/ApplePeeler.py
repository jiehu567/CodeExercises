# Flat 2D array to 1D array with clock-wise element selection

class ApplePeeler:
    def peel(self, nums):
        if not nums or not nums[0]:
            return []
        res, sr, sc, h, w = [], 0, 0, len(nums), len(nums[0])
        while True:
            if w==0 or h==0:
                break
            for c in range(sc, sc+w):
                res.append(nums[sr][c])
            sr += 1
            h -= 1
            if w==0 or h==0:
                break
            for r in range(sr, sr+h):
                res.append(nums[r][sc+w-1])
            w-=1
            if w==0 or h==0:
                break
            for c in range(sc+w-1, sc-1, -1):
                res.append(nums[sr+h-1][c]) 
            h-=1
            if w==0 or h==0:
                break
            for r in range(sr+h-1, sr-1, -1):
                res.append(nums[r][sc])
            sc+=1
            w-=1
        return res

# Test
ap = ApplePeeler()
nums = [[1,2,3,4],[10, 11, 12, 5], [9, 8, 7, 6]]
ap.peel(nums)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
