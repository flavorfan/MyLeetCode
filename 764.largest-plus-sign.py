#
# @lc app=leetcode id=764 lang=python3
#
# [764] Largest Plus Sign
#

# @lc code=start
# dp 1988 ms 81.25%
from typing import List
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0
        
        for r in range(N):
            count = 0
            for c in range(N):
                count = 0 if (r,c) in banned else count+1
                dp[r][c] = count
            
            count = 0
            for c in range(N-1, -1, -1):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        for c in range(N):
            count = 0
            for r in range(N):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
            
            count = 0
            for r in range(N-1, -1, -1):
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]
        
        return ans
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.orderOfLargestPlusSign(5,[[4,2]]))

