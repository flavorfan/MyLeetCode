#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # list to array 
    # 32ms 58.2%
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None or head.next is None:
            return None
        
        result = []
        while head:
            result.append(head)
            head = head.next
        
        if n == 1: 
            result[-2].next = None
            return result[0]
        
        if n == len(result):
            return result[1]

        result[-n-1].next = result[-n+1]
        return result[0]
    '''
    # 28ms 83.84%
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a1 = head
        prev = curr = nafter = a1 
        if a1.next == None: return None 
        for i in range(1,n):
            nafter = nafter.next 
        
        while(True):
            if nafter.next == None:
                if prev == curr : return curr.next
                prev.next = curr.next 
                break 
            prev = curr
            curr = curr.next 
            nafter = nafter.next

        return a1 


# @lc code=end

if __name__ == '__main__':
    sln = Solution()

    # 
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    # 
    head = sln.removeNthFromEnd(n1, 2)
    while head:
        print(head.val)
        head = head.next

    # print()


