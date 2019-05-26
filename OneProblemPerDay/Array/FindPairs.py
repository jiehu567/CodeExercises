# Find paris in an array with sum equal to target

class Program:
    def findPairs(self, nums, target):
        cnt = 0
        d = [0] * (target + 1)
        for i in range(len(nums)):
            diff = target - nums[i]
            if d[diff] != 0:
                cnt += 1
                d[diff] -= 1
            else:
                d[nums[i]] += 1
        return cnt

# Test case
p = Program()
p.findPairs([20, 260, 260, 20, 500, 500], 520)
# 3