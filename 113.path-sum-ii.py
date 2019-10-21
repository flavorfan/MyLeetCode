#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_recursive:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # DFS solution
        if not root:
            return [] 
        if root.left is None and root.right is None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []

        res = [] 
        left, right = [], []
        sum -= root.val
        
        if root.left:
            left = self.pathSum(root.left, sum)
        if root.right:
            right = self.pathSum(root.right, sum)
            
        for l in left:
            res.append([root.val] + l)
        for r in right:
            res.append([root.val] + r)
            
        return res

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if not root: 
            return ans

        stack = [(root, sum - root.val,[root.val])]  # de stored with (root, sum, path)

        while stack:
            node, curr_sum, path = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                ans.append(path[:])
            else:
                if node.right: 
                    stack.append((node.right, curr_sum - node.right.val, path + [node.right.val]))
                if node.left: 
                    stack.append((node.left, curr_sum - node.left.val, path + [node.left.val]))


        return ans
# @lc code=end

