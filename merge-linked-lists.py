"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Appraoch:
1. Create a dummy node to serve as the starting point of the merged list.
2. Use a pointer (current) to keep track of the last node in the merged list.
3. While both list1 and list2 are not empty, compare the values of the current nodes in both lists.
4. Append the smaller value node to the merged list and move the pointer of that list to the next node.
5. After the loop, one of the lists may still have remaining nodes. Append the remaining nodes to the merged list.
:P
"""
from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val = 0, next  = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next