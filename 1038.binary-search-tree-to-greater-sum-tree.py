#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # reverse indorder
    def bstToGst_old(self, root: TreeNode) -> TreeNode:
        def recur(node, sumTillNow):
            if not node: return sumTillNow 
            node.val += recur(node.right, sumTillNow)
            return recur(node.left, node.val)        
        recur(root, 0)
        return root 

    def bstToGst(self, root):
        self.getSums(root, 0)
        return root
    
    def getSums(self, node, sumGreaterTraversed):
        if not node.right and not node.left:
            node.val += sumGreaterTraversed       
        if node.right:
            node.val += self.getSums(node.right, sumGreaterTraversed)       
        if node.left:
            return self.getSums(node.left, node.val)        
        return node.val

