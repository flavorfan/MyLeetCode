#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# yield from 后面需要加的是可迭代对象 普通的可迭代对象，也可以是迭代器，甚至是生成器。


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val 
                yield from dfs(node.left)
                yield from dfs(node.right)
        
        return list(dfs(root1)) == list(dfs(root2))
        

