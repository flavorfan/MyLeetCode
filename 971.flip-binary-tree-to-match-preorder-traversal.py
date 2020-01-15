#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 28ms 94.8%
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.flipped = []
        self.i = 0 

        def dfs(node):
            if node:
                if  node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage)) and node.left and node.left.val != voyage[self.i]:
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        
        return self.flipped


# @lc code=end
if __name__ == '__main__':
    sln = Solution()
    # root = [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    voyage = [1,3,2]
    print(sln.flipMatchVoyage(root,voyage))

