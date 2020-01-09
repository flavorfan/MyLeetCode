#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#

# @lc code=start
# dp 108ms 16.41%
from typing import List
class Solution_1:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        # n1 表示数组 A 和 B 满足前 i - 1 个元素分别严格递增，并且 A[i - 1] 和 B[i - 1] 未被交换的最小交换次数，
        # 用 s1 表示 A[i - 1] 和 B[i - 1] 被交换的最小交换次数

        n1, s1 = 0, 1
        for i in range(1, len(A)):
            n2 = s2 = float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)        
                s2 = min(s2, s1 + 1)    
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)

            n1, s1 = n2, s2

        return min(n1, s1)

# 92ms 60.73%
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        #three case for ajacent pairs a[i],a[i-1],b[i],b[i-1].
        #1.a[i]<a[i-1] or b[i]<b[i-1],either one is not match,need to swap i or i-1 to be case 2.
        #2.no need to swap,if swap i,need to swap i-1 also
        #3.no need to swap,but swap also maintain ordered,min(a[i],b[i])>max(a[i-1],b[i-1])
        n=len(A)
        swap,noswap=1,0
        for i in range(1,n):
            if A[i]<=A[i-1] or B[i]<=B[i-1]:#case 1
                swap,noswap=noswap+1,swap
            elif min(A[i],B[i])>max(A[i-1],B[i-1]):#case 3,can do both
                swap,noswap=1+min(swap,noswap),min(swap,noswap)
            else:#case 2,noswap maintain, swap need to take previous swap status.
                swap+=1
        return min(swap,noswap)

# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    A = [1,3,5,4]
    B = [1,2,3,7]
    print(sln.minSwap(A,B))
