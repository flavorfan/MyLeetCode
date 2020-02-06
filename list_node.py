
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list_from_arr(arr):
    if len(arr) < 1: return None
    head = ListNode(arr[0])
    node = head
    for i in range(1,len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head

def print_list(head: ListNode):
    str_list = []
    a = head
    while a:
        str_list.append(str(a.val))
        a = a.next
    
    print_str =' > '.join(str_list)
    print(print_str)