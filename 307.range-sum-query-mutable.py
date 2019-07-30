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

    def __init__(self, nums: List[int]):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l-1,0,-1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1 | 1]
        

    def update(self, i: int, val: int) -> None:
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1
        

    def sumRange(self, i: int, j: int) -> int:
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res


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




