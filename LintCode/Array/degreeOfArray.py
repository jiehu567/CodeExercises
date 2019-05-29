# Degree of array
class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findShortestSubArray(self, nums):
        # write your code here
        counter = {}
        first = {}
        last = {}
        max_key = None
        max_cnt = 0
        for i, n in enumerate(nums):
            last[n] = i
            if n not in first:
                first[n] = i
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
            
            if not max_key or counter[n] > max_cnt:
                max_cnt = counter[n]
                max_key = n
        return last[max_key] - first[max_key] + 1