"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        # if N==0 :
        #     return 1

        for i in range(N):
            while (nums[i]>0 and nums[i]<N and nums[nums[i]-1] !=  nums[i]) :
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp

        for j in range(N):
            if nums[j] != j+1:
                return j+1

        #  deal with tail
        return N+1


if __name__ == '__main__':
    nums = [1,3,5,6]

    sln = Solution()
    print(sln.firstMissingPositive(nums))