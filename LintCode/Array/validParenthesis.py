class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stk = []
        for i in s:
            if i=='(' or i =='[' or i=='{':
                stk.append(i)
            else:
                if not stk:
                    return False
                elif i==']' and stk[-1] != '[' or \
                    i==')' and stk[-1] != '(' or  \
                    i=='}' and stk[-1] != '{':
                    return False
                else:
                    stk.pop()
        return len(stk) == 0