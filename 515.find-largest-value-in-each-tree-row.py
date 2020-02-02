#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
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
    def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        if not root : return ans 
        q = deque([root])
        while q:
            largest = float('-inf')
            level_len = len(q)
            for _ in range(level_len):
                node = q.popleft()
                largest = max(largest, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(largest)
        return ans
# @lc code=end

