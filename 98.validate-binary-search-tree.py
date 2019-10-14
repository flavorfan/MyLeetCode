#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_backtrace:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode,  lower = float('-inf'), upper = float('inf')):
            if not node: return True

            val = node.val
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.right,val , upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

class Solution_dfs:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True



# @lc code=end

