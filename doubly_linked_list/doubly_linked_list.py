"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
            self.length = 1
        else:
            self.head.insert_before(value)
            self.length += 1
            self.head = self.head.prev

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return None
        out = self.head.value
        if self.length < 2:
            self.head = None
            self.tail = None
            self.length = 0
            return out
        new = self.head.next
        self.head.delete()
        self.head = new
        self.length -= 1
        return out

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if not self.tail:
            self.head = ListNode(value)
            self.tail = self.head
            self.length = 1
        else:
            self.tail.insert_after(value)
            self.length += 1
            self.tail = self.tail.next

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if not self.tail:
            return None
        out = self.tail.value
        if self.length < 2:
            self.head = None
            self.tail = None
            self.length = 0
            return out
        new = self.tail.prev
        self.tail.delete()
        self.tail = new
        self.length -= 1
        return out

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        self.head.value, node.value = node.value, self.head.value

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        self.tail.value, node.value = node.value, self.tail.value

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.length < 2:
            self.head = None
            self.tail = None
            self.length = 0
        elif node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        max = self.head.value
        ptr = self.head
        c = 0
        while ptr is not None:
            if ptr.value > max:
                max = ptr.value
            ptr = ptr.next
        return max

    def printAll(self, *args):
        print()
        for arg in args:
            print(arg)
        ptr = self.head
        if self.length == 0:
            print(f'List empty! Head:{self.head} Tail:{self.tail}')
            return
        print(f'L:{len(self)}')
        while ptr is not None:
            print(f'V:{ptr.value}, P:{ptr.prev}, N:{ptr.next}')
            ptr = ptr.next
        print()
