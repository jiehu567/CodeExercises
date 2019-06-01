# Fraction Addition and Subtraction
class Solution:
    """
    @param expression: a string
    @return: return a string
    """
    def fractionAddition(self, expression):
        # write your code here
    
        # split string to number
        inputLst = self.getInputLst(expression)
        
        # loop all number string and calculate result
        result = inputLst[0]
        for i in range(1, len(inputLst)):
            result = self.add(result, inputLst[i])
        
        # return result
        return result
    
    def getInputLst(self, s):
        l, r = 0, 0
        res = []
        while r < len(s) and l < len(s):
            if r==len(s)-1:
                res.append(s[l:])
            elif s[r] == '-' and l!=r:
                res.append(s[l:r])
                l=r
            elif s[r] == '+' and l!=r:
                res.append(s[l:r])
                l=r+1
            r+=1
        return res
    
    def add(self, frac1, frac2):
        a, b = frac1.split('/')
        c, d = frac2.split('/')
        a,b,c,d = int(a),int(b),int(c),int(d)
        numeritor = a*d + b*c
        denominator = b*d
        sign = '' if numeritor * denominator >= 0 else '-'
        numeritor, denominator = abs(numeritor), abs(denominator)
        gcd = self.findGCD(numeritor, denominator)
        numeritor, denominator = numeritor // gcd, denominator // gcd
    
        return sign + str(numeritor) + '/' + str(denominator)
    
    def findGCD(self, a, b):
        if a==0:
            return b
        if b==0:
            return a
        
        a, b = max(a, b), min(a, b)
        r = a % b
        return self.findGCD(b, r)
    