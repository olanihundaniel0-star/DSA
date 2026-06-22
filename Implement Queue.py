# Implement Queue

def __init__(self):
    self.queue = []

def enqueue(self, value):
    self.queue.append(value)

def dequeue(self):
    if not self.queue:
        raise IndexError("Dequeue from an empty queue")
    return self.queue.pop(0)

def peek(self):
    if not self.queue:
        raise IndexError("Peek from an empty queue")
    return self.queue[0]

def is_empty(self):
    return len(self.queue) == 0

def __len__(self):
    return len(self.queue)

def __str__(self):
    return "Queue: " + str(self.queue)

def __eq__(self, other):
    return self.queue == other.queue

def __ne__(self, other):
    return self.queue != other.queue