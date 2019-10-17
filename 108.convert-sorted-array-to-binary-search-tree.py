#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
        begin = 0
        end = len(nums) - 1
        if begin > end:
            return None
        mid = (begin + end) >> 1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[begin:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:end+1])
        return root


if __name__ == '__main__':
    sln = Solution()
    nums = [-10,-3,0,5,9]
    sln.sortedArrayToBST(nums)

# @lc code=end

