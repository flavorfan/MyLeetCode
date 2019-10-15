#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 利用了搜索二叉树的中序遍历有序性找被替换的节点
# Inorder-traversal of the whole tree,
# The normal printed order is sorted. :D
# During it, mark down each pair of (pre, cur) nodes which (pre.val > cur.val).
# If 2 pairs found, then in (pre1, cur1, pre2, cur2), pre1 & cur2 are the swapped 2 nodes. See eg-1, eg-2.
# If 1 pair found, then in (pre1, cur1), pre1 & cur1 are the swapped 2 nodes. See eg-3.
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        stack, lower, nodes = [], TreeNode(float('-inf')),[]
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= lower.val:
                nodes += [lower, root]
            lower = root
            root = root.right
            
        if len(nodes) == 2:
            nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
        elif len(nodes) == 4:
            nodes[0].val, nodes[3].val = nodes[3].val, nodes[0].val


        
# @lc code=end

