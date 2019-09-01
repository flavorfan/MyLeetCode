#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from typing import List
class Solution:
    def minCostClimbingStairs_my(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]
        for i in range(2,len(cost)):
            dp.append( min(dp[i-1],dp[i-2])+ cost[i])
        return min(dp[-1], dp[-2])

    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
        
if __name__ == '__main__':
    sln = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(sln.minCostClimbingStairs(cost))

# dp[0] = cost[0]
# dp[1] = cost[1]
# dp[2] = min( dp[0],dp[1])  + cost[2] 
# dp[n] = Math.min(dp[n-1],dp[n-2]) + cost[n]
# f(i)=cost[i]+min{f(i−1),f(i−2)}.


