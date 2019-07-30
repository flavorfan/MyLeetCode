"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(inorder, postorder):
            if not inorder or not postorder:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)
            idx = inorder.index(root_val)

            root.right = helper(inorder[idx+1:],postorder)
            root.left = helper(inorder[:idx], postorder)

            return root

        return helper(inorder,postorder)


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    sln = Solution()
    print(sln.buildTree(inorder,postorder))