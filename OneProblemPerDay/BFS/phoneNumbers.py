# BFS version:
class Solution:

    def combinations(self, digits):
        
        if not digits:
            return []
        
        d = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],  
            '4': ['g','h','i'], 
            '5': ['j','k','l'], 
            '6': ['m','n','o'], 
            '7': ['p','q','r','s'], 
            '8': ['t','u','v'], 
            '9': ['w','x','y', 'z']      
            }
        
        res = []
        from collections import deque
        q = deque()
        q.append('')
        while q:
            cur = q.popleft()
            if len(cur) == len(digits):
                res.append(cur)
            else:
                for c in d[digits[len(cur)]]:
                    q.append(cur + c)
        return res

# Test case
s = Solution()
'ilovecsharp' in s.combinations('45683274277')
# True