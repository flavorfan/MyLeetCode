#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution_recursive:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        left = root.left
        right = root.right
        while left:
            left.next = right
            left = left.right
            right = right.left       
        self.connect(root.left)
        self.connect(root.right)

        return root 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left: 
            return root 
        root.left.next = root.right
        cur = root.left.left 
        pre = root.left 

        while cur:
            while pre:
                pre.left.next =pre.right
                if pre.next : 
                    pre.right.next = pre.next.left
                # else:
                #     pre.right.next = None
                pre = pre.next
            pre = cur
            cur = cur.left

        return root        
# @lc code=end

