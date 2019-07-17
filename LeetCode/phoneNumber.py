class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = [' ', None, 'abc', 'edf', 'ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        from collections import deque
        queue = deque([''])
        
        while queue:
            cur = queue.popleft()
            if len(cur) == len(digits):
                res.append(cur)
            else:
                for c in phone[int(digits[len(cur)])]:
                    queue.append(cur + c)
        
        return res