#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#
from typing import List
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for i,x in enumerate(S):
            if x == C:
                prev = i
            ans.append(i-prev)
        
        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i],prev - i)
        
        return ans
        

if __name__ == "__main__":
    sln = Solution()
    S = "loveleetcode"
    C = 'e'
    print(sln.shortestToChar(S, C))

