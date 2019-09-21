#
# @lc app=leetcode id=964 lang=python3
#
# [964] Least Operators to Express Number
#
from functools import lru_cache
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        cost = list(range(40))
        cost[0] = 2

        # 这个装饰器实现了备忘的功能，是一项优化技术，
        # 把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。
        # lru 是（least recently used）的缩写

        @lru_cache(None)
        def dp(i, targ):
            if targ == 0 : return 0
            if targ == 1 : return cost[i]
            if i >= 39 : return float('inf')
            
            # 返回一个包含商和余数的元组(a // b, a % b)
            t, r = divmod(targ , x)
            return min( r * cost[i] + dp(i + 1, t), 
                    (x-r) * cost[i] + dp(i + 1,t+1))
        
        return dp(0, target) - 1
        

if __name__ == "__main__":
    sln = Solution()
    print(sln.leastOpsExpressTarget(3,19))

