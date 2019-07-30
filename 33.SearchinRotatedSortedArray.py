"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rot_idx(left,right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot+1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot -1
                    else:
                        left = pivot + 1

        def search(left,right):
            while left<= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if target < nums[mid]:
                        right = mid -1
                    else:
                        left = mid + 1
            return -1

        n = len(nums)

        if n==0:
            return -1
        if n==1:
            return 0 if nums[0]== target else -1

        rot_idx = find_rot_idx(0,n-1)
        if nums[rot_idx] == target:
            return rot_idx
        if nums[rot_idx] > target:
            return -1

        if rot_idx == 0 :
            return search(0,n-1)

        if target < nums[0]:
            return search(rot_idx,n-1)
        return search(0,rot_idx)


if __name__ == '__main__':
    nums = [5,1,3]
    target = 3
    sln = Solution()
    print(sln.search(nums,target))