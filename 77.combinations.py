#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = [] ):
            if len(curr) == k:
                ans.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1,curr)
                curr.pop()
        ans = [] 
        backtrack() 
        return ans 

if __name__ == '__main__':
    n, k = 4, 2 
    sln = Solution() 
    print(sln.combine(n,k))

