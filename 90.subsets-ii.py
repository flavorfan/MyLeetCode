#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in sorted(nums):    # important sorted
            result += [i+[num] for i in result if i+[num] not in result]  # perfect
        return result
	

        
if __name__ == '__main__':
    nums = [1,2,2]
    sln = Solution()
    print(sln.subsetsWithDup(nums))
    pass
