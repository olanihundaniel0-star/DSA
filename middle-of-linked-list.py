"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Used Fast and slow pointer approach
"""
from typing import ListNode
from typing import Optional
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow =  head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
