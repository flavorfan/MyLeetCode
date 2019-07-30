"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {num: i for i,num in enumerate(nums)}

        for i in range(len(nums)):
            if ( (target - nums[i]) in nums_dict) and (i != nums_dict[target - nums[i]]):
                return [i, nums_dict[target - nums[i]]]
        return  None

if __name__ == '__main__':
    nums = [2, 7, 11, 15]

    target = 9
    sln = Solution()
    print(sln.twoSum(nums,target))