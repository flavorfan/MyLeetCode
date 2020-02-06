#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

from list_node import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

class Solution:
    # 32ms 84.35%
    '''
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: 
            return None
        l = []
        a = head
        while a: 
            l.append(a)
            a = a.next
        
        i = k % len(l)
        if i != 0:
            l[-i-1].next = None
            l[-1].next = head
            head = l[-i]
        return head
    '''
    # 28ms 96.36%
    # 36ms 60.59%
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        def get_length(head):
            length = 0
            a = head
            while a:
                length += 1
                a = a.next
            
            return length
        
        n = get_length(head)
        if n <= 1:
            return head 
        
        k = k % n 
        if k == 0:
            return head 
        
        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next

        new_head = curr = new_tail.next
        new_tail.next = None

        while curr.next: 
            curr = curr.next 
        curr.next = head

        return new_head
    

# @lc code=end

if __name__ == '__main__':
    sln = Solution()

    arr = [0,1,2,3,4,5]
    k = 2 

    head = make_list_from_arr(arr)
    print_list(sln.rotateRight(head,k))
    
