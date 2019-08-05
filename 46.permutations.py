#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n:
                ans.append(nums[:])
            for i in range(first, n):
                nums[first],nums[i] = nums[i], nums[first]
                backtrack( first +1)
                nums[first],nums[i] = nums[i], nums[first]
        n = len(nums)
        ans = []
        backtrack()
        return ans 

if __name__ == "__main__":
    nums = [1,2,3]
    sln = Solution()
    print(sln.permute(nums))
    


