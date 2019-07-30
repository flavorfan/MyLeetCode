"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        left = 0
        right = N-1
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return N
        while left <= right :
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else :
                right = mid -1
        return left


if __name__ == '__main__':
    nums = [1,3,5,6]

    target = 2
    sln = Solution()
    print(sln.searchInsert(nums,target))