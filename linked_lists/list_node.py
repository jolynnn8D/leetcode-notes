from typing import Optional 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        arr = []
        curr = self
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return str(arr)


def list_to_ll(input_list: list) -> Optional[ListNode]:
    head = curr = None
    for elem in input_list:
        node = ListNode(elem)
        if not head:
            head = curr = node
        else:
            curr.next = node
            curr = curr.next
    return head