class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def fourSumCount(self, A, B, C, D):
        # Write your code here
        cd = {}
        for cc in C:
            for dd in D:
                if cc+dd not in cd:
                    cd[cc+dd] = 1
                else:
                    cd[cc+dd]+=1
        cnt = 0
        for aa in A:
            for bb in B:
                if -(aa+bb) in cd:
                    cnt += cd[-(aa+bb)]
        return cnt