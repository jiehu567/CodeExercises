class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # Write your code here
        # import heapq
        # heapq.heapify(nums)
        # topk = heapq.nlargest(k, nums)
        # topk.sort()
        # topk.reverse()
        # return topk
        if not nums or len(nums) <= k:
            return sorted(nums, reverse=True)
        
        self.quickselect(nums, 0, len(nums)-1, k)
        return sorted(nums, reverse=True)[:k]
    
    def quickselect(self, nums, start, end, k):
        if start >= end:
            return
        
        l, r = start, end
        pivot = nums[start]
        while l<=r:
            while l<=r and nums[l] < pivot:
                l+=1
            while l<=r and nums[r] > pivot:
                r-=1
            if l<=r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        
        if r - start + 1 >= k:
            self.quickselect(nums, start, r, k)
        if l - start + 1 <= k:
            self.quickselect(nums, l, end, k - (l-start))