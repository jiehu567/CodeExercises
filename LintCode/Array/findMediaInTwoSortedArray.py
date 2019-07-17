class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
    
        m, n = len(A), len(B)
        import sys
        lo, hi = 0, len(A)
        while lo <= hi:
            partitionX = (lo + hi) // 2
            partitionY = (m+n+1) // 2 - partitionX
            
            leftMaxX = -sys.maxsize if partitionX == 0 else A[partitionX-1]
            rightMinX = sys.maxsize if partitionX == len(A) else A[partitionX]
            leftMaxY = -sys.maxsize if partitionY == 0 else B[partitionY-1]
            rightMinY = sys.maxsize if partitionY == len(B) else B[partitionY]
            
            if leftMaxX <= rightMinY and leftMaxY <= rightMinX:
                if (m + n) % 2 == 0:
                    return (max(leftMaxX, leftMaxY) + min(rightMinX, rightMinY))/2.0
                else:
                    return float(max(leftMaxX, leftMaxY))
            elif leftMaxX > rightMinY:
                hi = partitionX - 1
            else:
                lo = partitionX + 1
        return None