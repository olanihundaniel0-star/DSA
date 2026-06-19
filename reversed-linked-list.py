# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional
from git import ListNode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # sets previous to None
        curr = head # the current node is basically your head, im starting from the first index(node)

        while curr: # while curr is true
            nxt = curr.next # saves your next pointer before resetting
            curr.next = prev # sets your next pointer to previous
            prev = curr # then previous becomes the old current 
            curr = nxt # then your new current becomes next

        return prev 