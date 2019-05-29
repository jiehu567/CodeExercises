# Longest Common Prefix
class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        end = 0
        min_len = min([len(s) for s in strs])
        while end < min_len:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i-1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]