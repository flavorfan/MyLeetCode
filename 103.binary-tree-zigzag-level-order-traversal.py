#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        res = []
        turn = True
        while queue:
            curlevel = []
            levelsize = len(queue)
            for _ in range(levelsize):
                node = queue.popleft()
                curlevel.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right) 
            if turn:         
                res.append(curlevel)
            else:
                res.append(reversed(curlevel))
            turn = not turn
        return res
        
        

