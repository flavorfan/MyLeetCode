#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#
from typing import List
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        for i in range(len(A)-1,-1,-1):
            carry, A[i] = divmod(A[i],10)
            if i : A[i-1] += carry
        if carry: 
            # A = [ carry ] + A
            # A.insert(0,carry)
            A = list(map(int, str(carry))) + A
        return A


if __name__ == "__main__":
    sln = Solution()
    A = [0]
    K = 100
    print(sln.addToArrayForm(A,K))
