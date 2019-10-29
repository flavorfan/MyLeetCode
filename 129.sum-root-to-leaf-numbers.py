#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0

        de = [(root,root.val)]
        ans = 0
        while de:
            node, path_cout = de.pop()
            if not node.left and not node.right:
                ans += path_cout 
            
            if node.left:
                de.append((node.left, path_cout * 10 + node.left.val))
            if node.right: 
                de.append((node.right,path_cout * 10 + node.right.val))
        return ans

        
# @lc code=end

