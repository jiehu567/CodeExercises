class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        max_l = 1
        res = s[0]
        for c in range(len(s)):
            max_1, s1, e1 = self.helper(s, c, c)
            max_2, s2, e2 = self.helper(s, c, c+1)
            if max_l < max_1:
                max_l = max_1
                res = s[s1:e1+1]
            if max_l < max_2:
                max_l = max_2
                res = s[s2:e2+1]
        return res
    
    def helper(self, s, l, r):
        while l>=0 and r < len(s):
            if s[l] != s[r]:
                break
            l-=1
            r+=1
        return (r-l-1, l+1, r-1)
    