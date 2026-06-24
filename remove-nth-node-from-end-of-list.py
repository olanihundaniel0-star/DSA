# Given the head of a linked list, remove the nth node from the end of the list and return its head.
from typing import Optional
from typing import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        front = dummy
        back = dummy

        for i in range(n + 1):
            front = front.next
        while front is not None:
            front = front.next
            back = back.next

        back.next = back.next.next
        return dummy.next
        
