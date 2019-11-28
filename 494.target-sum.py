#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List
import collections
# @lc code=start
class Solution:
    def findTargetSumWays_1(self, nums: List[int], S: int) -> int:
        def dfs(cur, i, d = {}):
            if i < len(nums) and (i, cur) not in d: 
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))
        
        return dfs(0, 0)
    def findTargetSumWays_2(self, nums: List[int], S: int) -> int:
        def dfs(i, my_sum, cache={}):
            if (i, my_sum) not in cache:
                if i == len(nums):
                    cache[(i, my_sum)] = 1 if my_sum == S else 0
                else:
                    cache[(i, my_sum)] = dfs(i + 1, my_sum + nums[i]) + dfs(i + 1, my_sum - nums[i])
            return cache[(i, my_sum)]

        return dfs(0, 0)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums or sum(nums)<S: return 0
        dic = {0:1}
        for i in range(len(nums)):
            temp_dic = collections.defaultdict(int)
            for k in dic:
                temp_dic[k+nums[i]] += dic[k]
                temp_dic[k-nums[i]] += dic[k]
            dic = temp_dic
        return dic[S]
        
# @lc code=end
if __name__ == '__main__':
    sln = Solution()
    nums = [27,22,39,22,40,32,44,45,46,8,8,21,27,8,11,29,16,15,41,0]
    S = 10
    print(sln.findTargetSumWays(nums,S))
