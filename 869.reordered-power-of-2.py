#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#
import collections
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = collections.Counter(str(N))
        return any( count == collections.Counter(str(1 << b)) 
                for b in range(31) )

if __name__ == '__main__':
    sln = Solution()
    print(sln.reorderedPowerOf2(1))
