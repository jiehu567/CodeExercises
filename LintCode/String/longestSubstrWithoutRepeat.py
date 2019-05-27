class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        lo, window, d = 0, 0, {}
        for hi, c in enumerate(s):
            if c in d:
                lo = max(lo, d[c]+1)
            window = max(window, hi-lo+1)
            d[c] = hi
        return window