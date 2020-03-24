
import sys
sys.path.append('../doubly_linked_list')

# Queues
# * Should have the methods: `enqueue`, `dequeue`, and `len`.
# * `enqueue` should add an item to the back of the queue.
# * `dequeue` should remove and return an item from the front of the queue.
# * `len` returns the number of items in the queue.
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        out = self.storage.remove_from_head()
        return out

    def len(self):
        return self.storage.length
