#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# dp(i, j, N) = dp(i + 1, j, N - 1) + dp(i - 1, j, N - 1) + dp(i, j + 1, N - 1) + dp(i, j - 1, N - 1)


# @lc code=start
from functools import lru_cache
class Solution_lru:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        @lru_cache(None)
        def dp(i, j, N):
            if i < 0 or i >= m or j < 0 or j >= n :
                return int(N >= 0)
            elif N < 0:
                return 0
            res = 0
            for k in (1, -1):
                res += dp( i + k, j,N-1) + dp( i, j + k, N - 1 )
            return res 
        
        return dp(i, j, N) % ( 10 ** 9 + 7)

# 132ms 82.6%
# O(N*m*n) Space: 2*(m+2)*(n+2)
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[1] * (n + 2)]        
        for idx in range(m):
            dp.append([1] + [0] * n + [1])
        dp.append([1] * (n + 2))
        # ?? 
        for lev in range(0, N):
            new = [[1] * (n + 2)]        
            for idx in range(m):
                new.append([1] + [0] * n + [1])
            new.append([1] * (n + 2))
            for p in range(1, m + 1):
                for q in range(1, n + 1):
                    new[p][q] = dp[p-1][q] + dp[p][q-1] + dp[p][q+1] + dp[p+1][q]
            dp = new
        return (dp[i+1][j+1]) % (10 ** 9 + 7)
# @lc code=end

if __name__ == '__main__':
    sln =Solution()
    print(sln.findPaths(2,2,2,0,0))