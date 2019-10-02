#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            curlevel = []
            levelsize = len(queue)
            for _ in range(levelsize):
                node = queue.popleft()
                curlevel.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.insert(0,curlevel)
        return res
if __name__ == "__main__":

    pass
# @lc code=end

