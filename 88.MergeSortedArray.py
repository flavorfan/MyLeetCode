"""
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        pos = m+n-1
        while j >= 0 : # To be fix
            if i <0:
                nums1[j] = nums2[j]
                j -= 1
                continue
            if  nums1[i] >= nums2[j]:
                nums1[pos] = nums1[i]
                pos -= 1
                i -= 1
            else:
                nums1[pos] = nums2[j]
                pos -= 1
                j -= 1
        return  nums1



if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3

    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1

    sln = Solution()
    print(sln. merge(nums1, m, nums2, n))
