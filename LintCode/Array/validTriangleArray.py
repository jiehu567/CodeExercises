# Valid Triangle Array
class Solution:
    """
    @param nums: the given array
    @return:  the number of triplets chosen from the array that can make triangles
    """
    def triangleNumber(self, nums):
        # Write your code here
        nums = sorted(nums)
        total = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            end = i+2
            for j in range(i+1, len(nums)-1):
                while end < len(nums) and nums[i]+nums[j]>nums[end]:
                    end += 1
                total += end - 1 - j
        return total