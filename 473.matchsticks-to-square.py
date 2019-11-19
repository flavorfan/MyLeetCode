#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
from typing import List

# @lc code=start
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = sorted(nums,reverse=True)
        s = sum(nums)
        if n < 4:
            return False
        if s % 4 != 0:
            return False

        target = s/4
        visited = [0 for i in range(n)]
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                temp = self.dfs(nums,nums[i],i,target,visited,n)
                if temp[0] == False:
                    return False
                visited = temp[1]
        return True
    def dfs(self,nums,cur,i,target,visited,n):
        if cur == target:
            return [True,visited]
        for k in range(i+1,n):
            if not visited[k] and nums[k] + cur <= target:
                visited[k] = 1
                temp = self.dfs(nums,cur + nums[k],k,target,visited,n)
                if temp[0] == True:
                    return temp
                visited[k] = 0
        return [False,visited]   
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.makesquare([1,1,2,2,2]))
