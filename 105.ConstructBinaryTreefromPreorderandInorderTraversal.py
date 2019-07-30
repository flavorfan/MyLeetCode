"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(preorder,inorder):
            if not inorder:
                return None

            root_val = preorder.popleft()
            root = TreeNode(root_val)

            idx = inorder.index(root_val)

            root.left  = helper(preorder,inorder[:idx])
            root.right = helper(preorder,inorder[idx+1:])

            return root
        return helper(deque(preorder),inorder)

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # construct hashmap mapping a value to its inorder index
        idx = {}
        for i, val in enumerate(inorder):
            idx[val] = i

        # Iterate over preorder and construct the tree
        stack = []
        head = None
        for val in preorder:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if idx[val] < idx[stack[-1].val]:
                    stack[-1].left = node
                else:
                    while stack and idx[stack[-1].val] < idx[val]:
                        u = stack.pop()
                    u.right = node
                stack.append(node)
        return head



if __name__ == '__main__':
    # preorder = [3, 9, 20, 15, 7]
    # inorder = [9, 3, 15, 20, 7]

    preorder =  [3, 9, 20, 15, 7]
    inorder =[9, 3, 15, 20, 7]

    sln = Solution()
    print(sln.buildTree(preorder,inorder))
