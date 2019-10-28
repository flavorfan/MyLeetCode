#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution_bsp:
    def connect(self, root: 'Node') -> 'Node':
        if not root: 
            return root
        
        queue = [root,]
       
        tail = root 
        while queue:
            cur = queue.pop(0)
            if cur.left: 
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            
            if cur == tail:
                cur.next = None 
                tail = queue[-1] if len(queue) > 0 else None 

            else:
                cur.next = queue[0]
        return root 
            
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(-1, None, None, None)
        tmp = dummy
        res = root
        while root:
            while root:
                if root.left:
                    tmp.next = root.left
                    tmp = tmp.next
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                root = root.next
            root = dummy.next
            tmp = dummy
            dummy.next = None
            
        return res            
        
        
# @lc code=end

