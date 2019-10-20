#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_backtrace:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False

        sum -= root.val
        if not root.left and not root.right:
            return (sum == 0)
        
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root: return False

        de = [(root, sum - root.val),]

        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0: 
                return True
            
            if node.left: 
                de.append((node.left, curr_sum - node.left.val))
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
        
        return False

# @lc code=end

