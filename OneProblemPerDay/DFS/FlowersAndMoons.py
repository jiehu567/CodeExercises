# F: Female; M: Male
# Input n - paris of females and males
# Output a list of all combinations
# Restriction: Female first, total number of Females seated must be larger than total Males seated

class Program:
    def findPermutations(self, n):
        res = []
        self.dfs(res, n, 1, 0, 'F')
        return res
    
    def dfs(self, res, n, fc, mc, items):
        if fc == n and mc == n:
            res.append(items)
            return
        
        
        if fc < n:
            self.dfs(res, n, fc+1, mc, items + 'F')
        if mc < fc:
            self.dfs(res, n, fc, mc+1, items + 'M')

# Test
p = Program()
p.findPermutations(3)
# ['FFFMMM', 'FFMFMM', 'FFMMFM', 'FMFFMM', 'FMFMFM']
