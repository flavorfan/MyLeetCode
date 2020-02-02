#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:return []
        stack,res=[(root,[str(root.val)])],[]
        while stack:
            temp,val=stack.pop()
            if not temp.left and not temp.right:
                res.append('->'.join(val))
            if temp.left:
                stack.append((temp.left,val+[str(temp.left.val)]))
            if temp.right:
                stack.append((temp.right,val+[str(temp.right.val)]))
        return res
        
# @lc code=end

