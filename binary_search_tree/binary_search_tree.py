import sys
sys.path.append('../queue_and_stack')
from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    def insert(self, value):
        if self.value > value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target and self.left:
            return self.left.contains(target)
        elif self.value < target and self.right:
            return self.right.contains(target)
        else:
            return False
    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        bft_queue = Queue()
        bft_queue.enqueue(node)
        while bft_queue.storage.length:
            current = bft_queue.dequeue()
            print(current.value)
            if current.left:
                bft_queue.enqueue(current.left)
            if current.right:
                bft_queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        dft_stack = Stack()
        dft_visited = {}
        dft_stack.push(node)
        while dft_stack.storage.length:
            current = dft_stack.pop()
            print(current.value)
            if current.left and id(current.left) not in dft_visited:
                dft_visited[id(current.left)] = current.left
                dft_stack.push(current.left)
            if current.right and id(current.right) not in dft_visited:
                dft_visited[id(current.right)] = current.right
                dft_stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)
