#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
import collections
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.appendleft(root)
        while q:
            most_left = q[-1].val 
            for _ in range(len(q)):
                node = q.pop()  
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
        return most_left


# @lc code=end
if __name__ == '__main__':
    sln = Solution()


