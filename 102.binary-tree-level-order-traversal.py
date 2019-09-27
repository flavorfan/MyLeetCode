#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        res = []
        queue.append(root)
        while queue:
            curlevel = []
            levelsize = len(queue)
            for _ in range(levelsize):
                node = queue.popleft()
                curlevel.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(curlevel)
        return res

        

