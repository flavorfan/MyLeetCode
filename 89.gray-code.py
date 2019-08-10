#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(n):
            ans = ans + [j + 2**i for j in ans][::-1]
        return ans 

if __name__ == '__main__':
    sln = Solution() 
    print( sln.grayCode(4))


