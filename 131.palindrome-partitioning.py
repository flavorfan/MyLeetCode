#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path):
            if not s:  
                res.append(path) 
                return  
            for i in range(len(s)):
                if s[:i+1] == s[i::-1]:  
                    dfs(s[i+1:],path + [s[:i+1]])  # backtrack
        res = [] 
        path = []
        dfs(s,path)
        return res 


if __name__ == '__main__':
    s = "aab"
    sln = Solution()
    print(sln.partition(s))
    pass
