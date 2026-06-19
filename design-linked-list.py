class Node:
    def __init__(self, val):
        self.val = val # initialising value
        self.next = None # initialising pointer


class MyLinkedList:

    def __init__(self):
        self.head = None # first node
        self.size = 0          # needed for get() validation

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: # keeps index within range // accounts
            return -1
        curr = self.head # current value is first
        for _ in range(index):
            curr = curr.next # iterate to get value at index
        return curr.val # returns value

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)  # initialise node value
        new_node.next = self.head # next node
        self.head = new_node 
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


    

     

       