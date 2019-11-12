#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# Definition for a binary tree node.
# we construct a dp tree, each node in dp tree represents [stole the current node how much you gain, don't stole the current node how much you gain]
# dp_node[0] =[stole the current node how much you gain]
# dp_node[1] =[don't stole the current node how much you gain]
# we start the stolen from the leaf: Depth First Search
# for a node you have 2 opitions:
# option 1: stolen the node, then you can't stolen the child of the node. dp_node[0] = node.val + dp_node.left[1] +dp_node.right[1]
# option 2: don't stolen the node, then you can stolen th child of the node. dp_node[1] = dp_node.left[0] + dp_node.right[0]
# the maximum of gain of the node depents on max(dp_node[0],dp_node[1])

    """
    Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /   \          \
 1   2   1      [1,0]  [2,0]     [1,0]
 
    
    
    """    
# @lc code=start

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))
    
    def dfs(self, root: TreeNode):
        if not root: return (0, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))

        
# @lc code=end

