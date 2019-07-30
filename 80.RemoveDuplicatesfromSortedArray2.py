"""
80. Remove Duplicates from Sorted Array II
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        First =True
        i = 0
        for j in range(1,n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                First = True
            elif First:
                i += 1
                nums[i] = nums[j]
                First = False
        return i+1





if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    sln = Solution()
    print(sln.removeDuplicates(nums))