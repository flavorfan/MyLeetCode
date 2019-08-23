#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, val):
            if not node: return 

            new_val = val << 1 | node.val 

            if not node.left and not node.right: 
                self.ans += new_val  
            else:
                dfs(node.left, new_val)
                dfs(node.right, new_val)

        dfs(root, 0)
        return self.ans
        

