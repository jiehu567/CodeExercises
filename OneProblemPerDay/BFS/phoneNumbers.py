# BFS version:

# Optimized Solution, use array to replace dict

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def combinations(self, digits):
        # write your code here
        if not digits:
            return []
        phone = [None, None, 'abc', 'def', 'ghi', 'jkl','mno','pqrs','tuv','wxyz']
        from collections import deque
        q = deque()
        q.append('')
        res = []
        while q:
            cur = q.popleft()
            if len(cur) == len(digits):
                res.append(cur)
            else:
                for c in phone[int(digits[len(cur)])]:
                    q.append(cur+c)
        return res

# Traditional solution using dict
# class Solution:

#     def combinations(self, digits):
        
#         if not digits:
#             return []
        
#         d = {
#             '2': ['a','b','c'],
#             '3': ['d','e','f'],  
#             '4': ['g','h','i'], 
#             '5': ['j','k','l'], 
#             '6': ['m','n','o'], 
#             '7': ['p','q','r','s'], 
#             '8': ['t','u','v'], 
#             '9': ['w','x','y', 'z']      
#             }
        
#         res = []
#         from collections import deque
#         q = deque()
#         q.append('')
#         while q:
#             cur = q.popleft()
#             if len(cur) == len(digits):
#                 res.append(cur)
#             else:
#                 for c in d[digits[len(cur)]]:
#                     q.append(cur + c)
#         return res

# Test case
s = Solution()
'ilovecsharp' in s.combinations('45683274277')
# True