import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        out = self.storage[0]
        self.storage[0] = self.storage[len(self.storage)-1]
        self.storage.pop()
        self._sift_down(0)
        return out

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return
        parent = math.ceil((index/2)-1)
        if self.storage[index] > self.storage[parent]:
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            self._bubble_up(parent)

    def _sift_down(self, index):
        left = index*2+1
        right = left+1
        if len(self.storage) < right:
            return
        if len(self.storage) == right:
            if self.storage[index] < self.storage[left]:
                self.storage[index], self.storage[left] = self.storage[left], self.storage[index]
                self._sift_down(left)
            return
        if self.storage[index] < self.storage[right] and self.storage[right] > self.storage[left]:
            self.storage[index], self.storage[right] = self.storage[right], self.storage[index]
            self._sift_down(right)
        elif self.storage[index] < self.storage[left]:
            self.storage[index], self.storage[left] = self.storage[left], self.storage[index]
            self._sift_down(left)
