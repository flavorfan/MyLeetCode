#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (27.56%)
# Total Accepted:    66.4K
# Total Submissions: 240.3K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i
# to val.
# 
# Example:
# 
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# Note:
# 
# 
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
# 
# 
#
from typing import List
class NumArray:

    def __init__(self, nums):
        self.width = int(len(nums)**0.5)    # width of each bin (apart from last)
        self.bin_sums = []                  # sum of each bin
        self.nums = nums
        for i, num in enumerate(nums):
            if i % self.width == 0:         # start a new bin
                self.bin_sums.append(num)
            else:                           # add to last bin
                self.bin_sums[-1] += num

    def update(self, i, val):
        bin_i = i // self.width
        diff = val - self.nums[i]
        self.bin_sums[bin_i] += diff        # update bin_sums
        self.nums[i] = val                  # update nums

    def sumRange(self, i, j):
        bin_i, bin_j = i // self.width, j // self.width
        range_sum = sum(self.bin_sums[bin_i:bin_j])         # sum of whole bins
        range_sum += sum(self.nums[bin_j*self.width:j+1])   # add partial last bin
        range_sum -= sum(self.nums[bin_i*self.width:i])     # subtract partial first bin
        return range_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
#    9
#   8 1
#  3 5

if __name__ == '__main__':
    nums = [2,4,5,7,8,9]
    sln = NumArray(nums)
    print (sln.sumRange(2 ,5))




