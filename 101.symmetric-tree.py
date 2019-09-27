#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def isMirrored(left: TreeNode, right: TreeNode) -> bool:
    #         if not left and not right: return True
    #         if not left or not right: return False
    #         return left.val == right.val and isMirrored(left.left, right.right) and isMirrored(left.right, right.left)
        
    #     if not root: return True
    #     return  isMirrored(root.left, root.right)
    
    def _check(self, p, q):
        if not p or not q:
            return p == q
        return p.val == q.val
    
    # iterative using node pairs
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        worklist = deque([(root.left, root.right)])
        while worklist:
            p, q = worklist.popleft()
            if not self._check(p, q):
                return False
            if p:
                worklist.append((p.left, q.right))
                worklist.append((p.right, q.left))
                
        return True
    


        


