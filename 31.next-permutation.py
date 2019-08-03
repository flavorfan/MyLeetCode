#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # step-1 find the right most pair where nums[i] > nums[i-1]
        i = j = len(nums) -1 
        while i > 0 and nums[i-1] >= nums[i] :
            i -= 1
        if i == 0:      # nums in descending order
            nums.reverse()
            return
        
        # step-2 exchange nums[i-1] and the right most element which larger than nums[i-1] 
        k = i-1
        while nums[j] <= nums[k] :
            j -= 1
        nums[k],nums[j] = nums[j], nums[k]

        # step-3 reverse from i to the end
        l,r =i, len(nums)-1
        while l < r :
            nums[l],nums[r] = nums[r],nums[l]
            l += 1 ; r -= 1


if __name__ == '__main__' :
    nums = [3,2,1]
    sln = Solution()
    sln.nextPermutation(nums)
    print(nums)
    sln.nextPermutation(nums)
    print(nums)
    sln.nextPermutation(nums)
    print(nums)
    sln.nextPermutation(nums)
    print(nums)
    sln.nextPermutation(nums)
    print(nums)
    sln.nextPermutation(nums)
    print(nums)
    sln.nextPermutation(nums)
    print(nums)
