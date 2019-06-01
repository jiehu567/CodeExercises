# DFS recursion

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
        self.dfs(res, '', digits, d)
        return res
    
    def dfs(self, res, cur, digits, d):
        if len(cur) == len(digits):
            res.append(cur)
            return
        
        for c in d[digits[len(cur)]]:
            self.dfs(res, cur + c, digits, d)


# DFS iterative

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
#         stk = ['']
#         while stk:
#             cur = stk.pop()
#             if len(cur) == len(digits):
#                 res.append(cur)
#             else:
#                 for c in d[digits[len(cur)]]:
#                     stk.append(cur + c)
#         return res


# Test
s = Solution()
s.combinations('23')