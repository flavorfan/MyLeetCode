#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from typing import List
class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:

    #     def backtrack(first = 0 ):
    #         if first == n:
    #             ans.append(nums[:])
    #         for i in range( first , n):
    #             if i!= first and nums[i] == nums[first]:
    #                 continue
    #             nums[first], nums[i] = nums[i], nums[first]
    #             backtrack(first + 1)
    #             nums[first], nums[i] = nums[i], nums[first]
    #     n = len(nums)
    #     ans = []
    #     backtrack()
    #     return ans

    def backtrack(self, nums, s, k):
        if len(s) == k:
            self.ans.append(s[:])
        for i in range( len(nums) ):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            s.append(nums[i])
            self.backtrack( nums[:i] + nums[i+1:], s, k)
            s.pop()
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        self.backtrack(nums,[],len(nums))
        return self.ans


if __name__ == "__main__":
    nums = [1,1,3]
    sln = Solution()
    print(sln.permuteUnique(nums))
