#
# @lc app=leetcode id=1080 lang=python3
#
# [1080] Insufficient Nodes in Root to Leaf Paths
#
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, limit, t_sum):
        if root.left == None and root.right == None:    # leaf
            if t_sum + root.val < limit:
                return False 
            return True
        else: 
            if root.left != None and not self.dfs(root.left, limit, t_sum + root.val): 
                root.left = None
            if root.right != None and not self.dfs(root.right, limit, t_sum + root.val):
                root.right = None
            
            if root.left == None and root.right == None:
                return False

            return True
        
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root == None: 
            return None
        else:
            if not self.dfs(root, limit, 0):
                return None

        return root




# if __name__ == '__main__':


